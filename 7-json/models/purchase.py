from pydentic import BaseModel

class Purchase:
    id: int
    user_id: int
    flowers: list[dict]
    total_price: float