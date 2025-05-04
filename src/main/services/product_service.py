# src/main/services/product_service.py
class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def create_product(self, product_data):
        return self.repository.add_product(product_data)

    def get_product(self, product_id):
        return self.repository.get_product(product_id)

    def update_product(self, product_id, update_data):
        return self.repository.update_product(product_id, update_data)

    def delete_product(self, product_id):
        return self.repository.delete_product(product_id)

    def list_products(self):
        return self.repository.list_products()
