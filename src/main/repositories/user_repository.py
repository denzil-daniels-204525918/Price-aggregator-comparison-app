# src/main/repositories/user_repository.py
from .repository import Repository
from src.main.user import User

class UserRepository(Repository[User, str]):
    pass