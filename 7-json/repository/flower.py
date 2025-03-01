from models.flower import Flower
from typing import Optional

class FlowerRepository:
    def __init__(self):
        self.flowers: list[Flower] = []
        self.next_id = len(self.flowers)+1

    def add(self, flower: Flower):
        flower.id = self.next_id
        self.flowers.append(flower)
        self.next_id += 1
        return flower.id

    def get_all(self):
        return self.flowers
    
    def get_by_id(self, id: int) -> Optional[Flower]:
        for flower in self.flowers:
            if flower.id == id:
                return flower
        return None
    



