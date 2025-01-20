from fastapi import FastAPI, Response

from .cars import create_cars

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")


# (сюда писать решение)
@app.get("/cars", response_model=list[dict])
def get_cars(page: int, limit: int):
    start = (page - 1) * limit
    end = start + limit
    return cars[start:end]

@app.get("/cars/{id}")
def get_cars(id: int):
    car_data = None
    for car in cars:
        if car["id"] == id:
            car_data = car
    if not car_data:
        raise HTTPException(status_code=404, detail="Car not found")
    return cars[id]

# (конец решения)
