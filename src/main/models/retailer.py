from pydantic import BaseModel, EmailStr
from typing import List, Optional
from src.main.product import Product  # Assuming you have a Product class

class Retailer(BaseModel):
    """
    Pydantic model representing a retailer with validation.
    Includes business logic methods for product management.
    """
    retailer_id: str
    name: str
    contact_info: str  # Changed to str to be more flexible than just email
    products: List[Product] = []  # Initialize empty product list

    def add_product(self, product: Product) -> None:
        """
        Add a product to the retailer's inventory
        """
        self.products.append(product)
        # In a real application, you might want to log this properly
        print(f"Product {product.name} added by {self.name}.")

    def remove_product(self, product: Product) -> bool:
        """
        Remove a product from the retailer's inventory
        Returns True if product was found and removed, False otherwise
        """
        if product in self.products:
            self.products.remove(product)
            print(f"Product {product.name} removed by {self.name}.")
            return True

        print(f"Product {product.name} not found in retailer's inventory.")
        return False

    class Config:
        # Pydantic configuration
        json_schema_extra = {
            "example": {
                "retailer_id": "retailer123",
                "name": "Awesome Store",
                "contact_info": "contact@awesomestore.com",
                "products": []
            }
        }
