from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# (сюда писать решение)
@app.get("/users")
def all_users(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("users/all_users.html", {"request" : request, "users" : users})

@app.get("/users/{id}", response_class=HTMLResponse)
def user_id(request: Request, id: int):
    # Поиск пользователя по id
    user_data = None
    for user in users:
        if user["id"] == id:
            user_data = user
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse(
        "users/user.html", {"request": request, "user": user_data, "id": id}
    )
# (конец решения)
