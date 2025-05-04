# services/price_service.py

from typing import List
from main.repositories.product_repository import ProductRepository
from main.product import Product

class PriceService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def get_product_price(self, product_id: str) -> float:
        """Retrieve the price of a product by its ID."""
        product = self.repo.find_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        return product.price

    def get_all_product_prices(self) -> List[float]:
        """Retrieve a list of all product prices."""
        products = self.repo.find_all()
        return [product.price for product in products]

    def update_product_price(self, product_id: str, new_price: float) -> Product:
        """Update the price of a product."""
        product = self.repo.find_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        product.price = new_price
        return self.repo.update(product_id, product)

    def apply_discount(self, product_id: str, discount_percentage: float) -> Product:
        """Apply a discount to the price of a product."""
        product = self.repo.find_by_id(product_id)
        if not product:
            raise ValueError(f"Product with ID {product_id} not found.")
        discounted_price = product.price * (1 - discount_percentage / 100)
        product.price = discounted_price
        return self.repo.update(product_id, product)

    def calculate_total_price(self, product_ids: List[str]) -> float:
        """Calculate the total price of a list of products."""
        total_price = 0
        for product_id in product_ids:
            total_price += self.get_product_price(product_id)
        return total_price
