# src/main/repositories/product_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from src.main.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Product]:
        pass

    @abstractmethod
    def find_all(self) -> List[Product]:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass

    @abstractmethod
    def update(self, product_id: str, product: Product) -> Product:
        """Update a product by its ID."""
        pass
