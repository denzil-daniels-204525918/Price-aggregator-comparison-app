# src/main/repositories/inmemory/inmemory_saved_list_repository.py

from src.main.repositories.repository import Repository
from typing import List, Optional
from src.main.saved_list import SavedList  # Assuming this exists

class InMemorySavedListRepository(Repository[SavedList, str]):
    def __init__(self):
        self._storage = {}  # In-memory dictionary

    def save(self, saved_list: SavedList) -> None:
        self._storage[saved_list.id] = saved_list

    def find_by_id(self, id: str) -> Optional[SavedList]:
        return self._storage.get(id)

    def find_all(self) -> List[SavedList]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
