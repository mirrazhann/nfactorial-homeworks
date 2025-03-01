from pydantic import BaseModel, validator

class Flower(BaseModel):
    id:int
    name: str
    count: int
    price: float

    @validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Цена должна быть больше нуля')
        return value
    
    @validator('count')
    def price_must_be_positive(cls, value):
        if value < 0:
            raise ValueError('Количество не может быть отрицательным')
        return value