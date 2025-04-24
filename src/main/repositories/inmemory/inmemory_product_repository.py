# src/main/repositories/inmemory/inmemory_product_repository.py

from typing import Optional, List
from src.main.product import Product
from src.main.repositories.product_repository import ProductRepository

class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._storage = {}

    def save(self, product: Product):
        self._storage[product.product_id] = product  # <-- MUST be product.product_id


    def find_by_id(self, id: str) -> Optional[Product]:
        return self._storage.get(id)

    def find_all(self) -> List[Product]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
