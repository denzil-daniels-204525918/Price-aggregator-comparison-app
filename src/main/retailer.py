# src/main/retailer.py

class RetailerModel:
    def __init__(self, retailer_id: str, name: str, contact_info: str):
        self.retailer_id = retailer_id
        self.name = name
        self.contact_info = contact_info
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product {product.name} added by {self.name}.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product {product.name} removed by {self.name}.")
        else:
            print(f"Product {product.name} not found in retailer's inventory.")


from pydantic import BaseModel, EmailStr

class Retailer(BaseModel):
    retailer_id: str
    name: str
    contact_info: EmailStr  # Using EmailStr for validation
