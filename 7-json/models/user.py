from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    password: str
    email: str
    foto: Optional[bytes] = None

   