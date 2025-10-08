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

    # Prototype method: Clone method using deepcopy
    def clone(self):
        return copy.deepcopy(self)

# Example of a Product Template to clone
milk_template = Product(product_id="001", name="Milk", price=3.50, description="1L Full Cream Milk")
