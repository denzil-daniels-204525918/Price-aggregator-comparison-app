from typing import Optional, List
from src.main.repositories.inmemory.inmemory_product_repository import InMemoryProductRepository
from src.main.product import Product  # Add this import

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