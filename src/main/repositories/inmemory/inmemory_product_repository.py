from typing import Optional, List
from src.main.product import Product  # Add this import

class InMemoryProductRepository:
    def __init__(self):
        self.storage = {}

    def save(self, product: Product) -> Product:
        self.storage[product.product_id] = product
        return product

    def find_by_id(self, product_id: str) -> Optional[Product]:
        return self.storage.get(product_id)

    def find_all(self) -> List[Product]:
        return list(self.storage.values())

    def delete(self, product_id: str) -> bool:
        if product_id in self.storage:
            del self.storage[product_id]
            return True
        return False

    def update(self, product: Product) -> Product:
        self.storage[product.product_id] = product
        return product