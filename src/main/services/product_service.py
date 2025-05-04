from typing import List
from main.repositories.product_repository import ProductRepository
from main.product import Product

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def add_product(self, name: str, category: str, price: float, description: str = "") -> Product:
        # Updated the Product instantiation to include 'product_id' and 'price'
        product = Product(product_id=None, name=name, price=price, category=category, description=description)
        return self.repo.save(product)

    def get_all_products(self) -> List[Product]:
        return self.repo.find_all()

    def get_product_by_id(self, product_id: str) -> Product:
        return self.repo.find_by_id(product_id)

    def get_products_by_category(self, category: str) -> List[Product]:
        # Filtering products by category
        return [p for p in self.repo.find_all() if p.category.lower() == category.lower()]

    def update_product(self, product_id: str, **kwargs) -> Product:
        # Find the existing product
        product = self.repo.find_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")

        # Update product attributes based on provided kwargs
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        return self.repo.update(product_id, product)

    def delete_product(self, product_id: str) -> bool:
        # Delete the product by its ID
        return self.repo.delete(product_id)
