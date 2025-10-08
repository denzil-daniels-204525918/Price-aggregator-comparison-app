# --- src/main/models/saved_list.py ---
class SavedList:
    def __init__(self, list_id: str, user_id: str):
        self.list_id = list_id
        self.user_id = user_id
        self.products = []

    def add_product_to_list(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to saved list {self.list_id}.")

    def remove_product_from_list(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product {product.name} removed from saved list {self.list_id}.")
        else:
            print(f"Product {product.name} not found in saved list {self.list_id}.")