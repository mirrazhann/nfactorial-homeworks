from models.user import User
from typing import Optional

class UserRepository():
    def __init__(self):
        self.users: list[User] = []
        self.next_id = 1
    
    def add(self, user: User):
        user.id = self.next_id
        self.users.append(user)
        self.next_id += 1
        return True
    
    def get_all(self):
        return self.users

    def find_user_by_email(self, email: str) -> Optional[User]:
        for user in self.users:
            if user.email.lower() == email.lower():
                return user
        return None

    def find_user_by_id(self, id: int) -> Optional[User]:
        for user in self.users:
            if user.id == id:
                return user
        return None 
        