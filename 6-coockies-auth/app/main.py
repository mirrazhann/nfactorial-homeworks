from fastapi import FastAPI, Request, Form, File, UploadFile, HTTPException, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta
import jwt
import base64
import json

from repository.user import UserRepository
from models.user import User

from repository.flower import FlowerRepository
from models.flower import Flower

SECRET_KEY = "flower_shop"
ALGORITHM = "HS256"


app = FastAPI()
templates = Jinja2Templates(directory="templates")
user = UserRepository()
flower = FlowerRepository()

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# регистрация
@app.get("/signup")
def get_signup(request: Request):
    return templates.TemplateResponse("user/signup.html", {"request": request})

@app.post("/signup")
async def post_signup(
    request: Request, 
    email: str = Form(),
    user_name: str = Form(),
    password: str = Form(),
    foto: UploadFile = File(None)
):
    if user.find_user_by_email(email):
        return HTMLResponse("Пользователь с таким емейлом уже зарегистрирован. <br><a href=\"/login\">Войти</a>")
    foto_bytes = await foto.read() if foto else None
    new_user = User(id = 0, name = user_name, password = password, email = email, foto = foto_bytes)
    user.add(new_user)
    # return templates.TemplateResponse("user/signup.html", {"request": request, "users": user.get_all()})
    return RedirectResponse(url = "/login", status_code = 302)

# Авторизация
@app.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("user/login.html", {"request": request})

@app.post("/login")
def post_login(
    request: Request,
    email: str = Form(),
    password: str = Form()
):
    temp_user = user.find_user_by_email(email)
    if not temp_user:
        return HTMLResponse(f"Неверный email {temp_user} <br><a href=\"/signup\">Регистрация</a>")
    elif temp_user.password != password:
        return HTMLResponse("Неверный парольl <br><a href=\"/signup\">Регистрация</a>")
    # генерим токен и сохраняем в куки (авторизация)
    token = create_token(temp_user)
    response = RedirectResponse(url = "/profile", status_code = 302)
    response.set_cookie(key = "token", value = token)
    return response

# Токен авторизации
def create_token(user: User):
    payload = {
        'user_id': user.id,
        "exp": datetime.utcnow() + timedelta(hours=1) 
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Проверка авторизации
def get_user(request: Request):
    token = request.cookies.get("token")
    if not token:
        return HTMLResponse("Пользователь не авторизирован <br><a href=\"/signup\">Регистрация</a><br><a href=\"/login\">Войти</a>")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        current_user = user.find_user_by_id(user_id)
        if not current_user:
            return HTMLResponse("Пользователь не найден <br><a href=\"/signup\">Регистрация</a><br><a href=\"/login\">Войти</a>")
        return current_user
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Неверный токен")
    
# Профиль
@app.get("/profile")
def get_profile(request: Request):
    try:
        current_user = get_user(request)
    except HTTPException as e:
        return HTMLResponse("Пользователь не авторизирован <br><a href=\"/signup\">Регистрация</a><br><a href=\"/login\">Войти</a>")
    photo_b64 = ""
    if current_user.foto:
        photo_b64 = base64.b64encode(current_user.foto).decode("utf-8")
    return templates.TemplateResponse("user/profile.html", {"request": request, "user": current_user, "photo_b64": photo_b64})

# Список цветов
@app.get("/flowers")
def get_flowers(request: Request):
    try:
        current_user = get_user(request)
    except HTTPException as e:
        return HTMLResponse("Пользователь не авторизирован <br><a href=\"/signup\">Регистрация</a><br><a href=\"/login\">Войти</a>")
    return templates.TemplateResponse("flower/list.html", {"request": request, "flowers": flower.get_all()})

# Добавление в список нового цветка
@app.post("/flowers")
def post_flowers(
    request: Request,
    flower_name: str = Form(),
    count: int = Form(),
    price: float = Form()
):
    new_flower = Flower(id=0, name = flower_name, count = count, price = price)
    flower.add(new_flower)
    return RedirectResponse(url = "/flowers", status_code = 302)


# Добавление цветка в корзину
@app.post("/cart/items")
def add_in_cart(
    request: Request,
    response: Response,
    flower_id: int = Form()
):
    cart = []
    cart_cookie = request.cookies.get('cart')
    if cart_cookie:
        try: 
            cart = json.loads(cart_cookie)
        except:
            cart = []
    cart.append(flower_id)
    response = RedirectResponse(url = "/flowers", status_code = 302)
    response.set_cookie(key = "cart", value = json.dumps(cart))
    return response

# Просмотр корзины
@app.get("/cart/items")
def get_cart(request: Request):
    try:
        current_user = get_user(request)
    except HTTPException as e:
        return HTMLResponse("Пользователь не авторизирован <br><a href=\"/signup\">Регистрация</a><br><a href=\"/login\">Войти</a>")
    cart = []
    cart_cookie = request.cookies.get("cart")
    if cart_cookie:
        try:
            cart = json.loads(cart_cookie)
        except:
            cart = []
    total = 0.0
    cart_flowers = []
    for flower_id in cart:
        flower_in_cart = flower.get_by_id(flower_id)
        if flower_in_cart:
            cart_flowers.append(flower_in_cart)
            total += flower_in_cart.price
    return templates.TemplateResponse("cart/index.html", {"request": request, "flowers": cart_flowers, "total_price": total})

# Добавление заказа
# @app.post("/purchased")
# def purchase(request: Request, response: Response):
#     try:
#         user = get_user(request)
#     except HTTPException as e:
#         return HTMLResponse("Пользователь не авторизирован <br><a href=\"/signup\">Регистрация</a><br><a href=\"/login\">Войти</a>")
#     cart = []
#     cart_cookie = request.cookies.get("cart")
#     if cart_cookie:
#         try:
#             cart = json.loads(cart_cookie)
#         except:
#             cart = []
#     for flower_id in cart:
#         purchase = Purchase(user_id=user.id, flower_id=flower_id)
#         purchases_repo.add_purchase(purchase)

#     response = RedirectResponse(url="/purchased", status_code=302)
#     response.delete_cookie("cart")
#     return response
# Список заказов





