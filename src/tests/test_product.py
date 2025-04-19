# src/main/clone_method.py

import copy

class Product:
    def __init__(self, product_id, name, price, description, store=None, availability=None, promotion=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.store = store
        self.availability = availability
        self.promotion = promotion

    def __str__(self):
        return (f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, "
                f"Description: {self.description}, Store: {self.store}, Availability: {self.availability}, "
                f"Promotion: {self.promotion}")

    # 🧱 Add product/update details
    def add_product(self, name, price, description):
        print(f"Product {self.name} updated to {name}.")
        self.name = name
        self.price = price
        self.description = description

    # 🗑️ Remove product/reset attributes
    def remove_product(self):
        print(f"Product {self.name} removed.")
        self.name = None
        self.price = None
        self.description = None
        self.store = None
        self.availability = None
        self.promotion = None

    # 🧬 Prototype: Clone method using deepcopy
    def clone(self):
        return copy.deepcopy(self)
