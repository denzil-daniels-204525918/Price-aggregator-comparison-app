# src/product.py

class Product:
    def __init__(self, product_id: str, name: str, price: float, description: str):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def add_product(self):
        # Logic to add product (simplified for demonstration)
        print(f"Product {self.name} added.")

    def remove_product(self):
        # Logic to remove product (simplified for demonstration)
        print(f"Product {self.name} removed.")
