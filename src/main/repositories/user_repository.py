# src/main/repositories/user_repository.py
from .repository import Repository
from price_aggregator.main.models.user import User

class UserRepository(Repository[User, str]):
    pass