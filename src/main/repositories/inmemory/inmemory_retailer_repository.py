from src.main.repositories.repository import Repository
from typing import List, Optional
from src.main.retailer import Retailer

class InMemoryRetailerRepository(Repository[Retailer, str]):
    def __init__(self):
        self._storage = {}

    def save(self, retailer: Retailer) -> None:
        self._storage[retailer.retailer_id] = retailer  # Ensure using `retailer_id`

    def find_by_id(self, id: str) -> Optional[Retailer]:
        return self._storage.get(id)

    def find_all(self) -> List[Retailer]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
