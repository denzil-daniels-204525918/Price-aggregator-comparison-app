# main/services/product_service.py

from main.product import Product  # Make sure to import the Product class

class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def create_product(self, name: str, category: str, description: str) -> Product:
        product_id = str(self.repository.get_next_id())  # Assuming we generate the ID this way.
        product = Product(product_id=product_id, name=name, category=category, description=description, price=0.0)
        self.repository.save(product)
        return product

    def get_all_products(self) -> list:
        return self.repository.find_all()

    def update_product(self, product_id: str, **kwargs) -> Product:
        product = self.repository.find_by_id(product_id)
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        self.repository.update(product_id, product)
        return product

    def delete_product(self, product_id: str) -> bool:
        return self.repository.delete(product_id)
