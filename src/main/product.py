# src/main/product.py

class Product:
    def __init__(self, product_id, name, price, category, description=""):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.description = description

from pydantic import BaseModel

class Product(BaseModel):
    product_id: str
    name: str
    price: float  # ✅ this line is essential
    category: str
    description: str
