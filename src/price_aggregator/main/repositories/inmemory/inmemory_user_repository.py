# src/main/repositories/inmemory/inmemory_user_repository.py

from price_aggregator.main.repositories.repository import Repository
from typing import List, Optional
from price_aggregator.main.models.user import User  # Assuming a User class exists with at least an `id` field

class InMemoryUserRepository(Repository[User, str]):
    def __init__(self):
        self._storage = {}  # In-memory storage using a dictionary

    def save(self, user: User) -> None:
        self._storage[user.id] = user

    def find_by_id(self, id: str) -> Optional[User]:
        return self._storage.get(id)

    def find_all(self) -> List[User]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
