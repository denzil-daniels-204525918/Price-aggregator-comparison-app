# src/main/repositories/inmemory/inmemory_product_repository.py
from typing import Dict, Optional

class InMemoryProductRepository:
    def __init__(self):
        self.products: Dict[str, dict] = {}

    def add_product(self, product_data: dict) -> dict:
        product_id = product_data["product_id"]
        self.products[product_id] = product_data
        return product_data

    def get_product(self, product_id: str) -> Optional[dict]:
        return self.products.get(product_id)

    def update_product(self, product_id: str, update_data: dict) -> Optional[dict]:
        if product_id in self.products:
            self.products[product_id].update(update_data)
            return self.products[product_id]
        return None

    def delete_product(self, product_id: str) -> bool:
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False

    def list_products(self) -> list:
        return list(self.products.values())
