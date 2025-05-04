# src/main/services/price_service.py
class PriceService:
    def __init__(self, repository):
        self.repository = repository

    def create_price(self, price_data):
        return self.repository.add_price(price_data)

    def get_price(self, price_id):
        return self.repository.get_price(price_id)

    def update_price(self, price_id, update_data):
        return self.repository.update_price(price_id, update_data)

    def delete_price(self, price_id):
        return self.repository.delete_price(price_id)

    def list_prices(self):
        return self.repository.list_prices()
