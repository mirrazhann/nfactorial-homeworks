from fastapi import FastAPI, Request, Form, File, UploadFile, HTTPException, Response, Depends
from fastapi.responses import HTMLResponse
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
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
user = UserRepository()
flower = FlowerRepository()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")
# регистрация

@app.post("/signup")
async def post_signup(
    request: Request, 
    email: str = Form(),
    user_name: str = Form(),
    password: str = Form(),
    foto: UploadFile = File(None)
):
    if email.strip() == "":
        result = {
            "result": "error",
            "message": "invalid email"
        }
        raise HTTPException(status_code=401, detail=result)
    elif user_name.strip() == "":
        result = {
            "result": "error",
            "message": "invalid user name"
        }
        raise HTTPException(status_code=401, detail=result)
    elif password.strip() == "":
        result = {
            "result": "error",
            "message": "invalid password"
        }
        raise HTTPException(status_code=401, detail=result)
    
    if user.find_user_by_email(email):
        result = {
            "result": "error",
            "message": "email was registered earley"
        }
        raise HTTPException(status_code=401, detail=result)
    foto_bytes = await foto.read() if foto else None
    new_user = User(id = 0, name = user_name, password = password, email = email, foto = foto_bytes)
    user.add(new_user)
    result = {
        "result": "ok",
        "message": "New user created"
    }
    return result

# Авторизация

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username  # здесь username выступает как email
    password = form_data.password
    temp_user = user.find_user_by_email(email)
    if not temp_user:
        result = {
            "result": "error",
            "message": "invalid email"
        }
        raise HTTPException(status_code=401, detail=result)
    elif temp_user.password != password:
        result = {
            "result": "error",
            "message": "invalid password"
        }
        raise HTTPException(status_code=401, detail=result)
    # генерим токен и сохраняем в куки (авторизация)
    token = create_token(temp_user)
    result = {
            "result": "ok",
            "access_token": token
        }
    return result

# Токен авторизации
def create_token(user: User):
    payload = {
        'user_id': user.id,
        "exp": datetime.utcnow() + timedelta(hours=1) 
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Проверка авторизации
def get_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            result = {
                "result": "error",
                "message": "Invalid credentials"
            }
            raise HTTPException(status_code=401, detail=result)
        # Получаем данные пользователя (в виде словаря) из репозитория
        user_data = user.find_user_by_id(int(user_id))
        if not user_data:
            result = {
                "result": "error",
                "message": "User not found"
            }
            raise HTTPException(status_code=401, detail=result)
        # Преобразуем словарь в объект User, если необходимо
        if isinstance(user_data, dict):
            user_obj = User(**user_data)
        else:
            user_obj = user_data
        return user_obj
    except jwt.PyJWTError:
        result = {
                "result": "error",
                "message": "Invalid credentials"
        }
        raise HTTPException(status_code=401, detail=result)
    
# Профиль
@app.get("/profile")
async def profile(current_user: User = Depends(get_user)):
    result = {
        "id": current_user.id,
        "email": current_user.email,
        "name": current_user.name,
    }
    foto_b64 = base64.b64encode(current_user.foto).decode() if current_user.foto else None
    result["foto"] = foto_b64
    return result

# Список цветов
@app.get("/flowers")
def get_flowers():
    flowers = flower.get_all()
    result = [{"id" : f.id, "name": f.name, "count": f.count, "price": f.price} for f in flowers]
    return result 

# Добавление в список нового цветка
@app.post("/flowers")
def post_flowers(
    current_user: User = Depends(get_user),
    flower_name: str = Form(),
    count: int = Form(),
    price: float = Form()
):
    # Если пользователь авторизован, он может добавить новый цветок в каталог
    new_flower = Flower(id=0, name = flower_name, count = count, price = price)
    new_flower_id = flower.add(new_flower)
    return {"flower_id": new_flower_id}


# Добавление цветка в корзину
@app.post("/cart/items")
def add_in_cart(
    request: Request,
    response: Response,
    flower_id: int = Form(),
    current_user: User = Depends(get_user)
):
    cart = []
    cart_cookie = request.cookies.get('cart')
    if cart_cookie:
        try: 
            cart = json.loads(cart_cookie)
        except:
            cart = []
    cart.append(flower_id)
    response.set_cookie(key = "cart", value = json.dumps(cart))
    return {"result": "ok", "message": "flower added to cart"}

# Просмотр корзины
@app.get("/cart/items")
def get_cart(request: Request, current_user: User = Depends(get_user)):
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
            flower_in_cart.count = 1
            cart_flowers.append(flower_in_cart)
            total += flower_in_cart.price
    result = {
        "items": cart_flowers,
        "total_price": total
    }
    return result

@app.delete("/cart/items")
async def clear_cart(response: Response):
    response.delete_cookie("cart")
    return {"result": "ok", "message": "Empty cart"}

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





