# --- src/main/services/product_service.py ---
from typing import Optional, List
from price_aggregator.main.repositories.inmemory.inmemory_product_repository import InMemoryProductRepository
from price_aggregator.main.models.product import Product

class ProductService:
    def __init__(self, repository: InMemoryProductRepository = None):
        self.repository = repository or InMemoryProductRepository()

    def create_product(self, product_data: dict) -> Product:
        product = Product(**product_data)
        return self.repository.save(product)

    def get_product(self, product_id: str) -> Optional[Product]:
        return self.repository.find_by_id(product_id)

    def get_all_products(self) -> List[Product]:
        return self.repository.find_all()

    def update_product(self, product_id: str, update_data: dict) -> Optional[Product]:
        product = self.repository.find_by_id(product_id)
        if not product:
            return None
        for key, value in update_data.items():
            setattr(product, key, value)
        return self.repository.update(product)

    def delete_product(self, product_id: str) -> bool:
        return self.repository.delete(product_id)
