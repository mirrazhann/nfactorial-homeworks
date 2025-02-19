from fastapi import FastAPI, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from repository.car import CarsRepository

app = FastAPI()
repository = CarsRepository()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cars/search")
def cars_get_form(request: Request, car_name: str = ""):
    if car_name != "":
        cars = repository.find(car_name)
        if cars != False:
            return templates.TemplateResponse("cars/search.html", {"request": request, "cars": cars, "car_name": car_name})
        else:
            return templates.TemplateResponse("cars/search.html", {"request": request, "car_name": car_name, "error": "Не найдено совпадений!"}) 
    else:
        return templates.TemplateResponse("cars/search.html", {"request": request, "car_name": car_name, "error": "Введите название!"}) 
    
@app.get("/cars/new")
def cars_get_form(request: Request):
    return templates.TemplateResponse("cars/new.html", {"request": request})


@app.post("/cars/new")
def cars_get_form(request: Request, car_name: str = Form(...), car_year: int = Form(...)):
    if car_year < 1900:
        return templates.TemplateResponse("cars/new.html", {"request": request, "car_name": car_name, "car_year": car_year, "error": "Не верный год выпуска!"}) 
    elif car_name == "":
        return templates.TemplateResponse("cars/new.html", {"request": request, "car_name": car_name, "car_year": car_year, "error": "Заполните название!"})
    repository.save({"name": car_name, "year": car_year})
    return RedirectResponse(url="/cars", status_code=303)

@app.get("/cars")
def get_all_cars(request: Request):
    cars = repository.get_all()
    return templates.TemplateResponse("cars/all_cars.html", {"request": request, "cars": cars})