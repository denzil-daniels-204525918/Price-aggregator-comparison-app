# src/main/services/price_service.py

from typing import List, Optional
from price_aggregator.main.models.price import Price
from price_aggregator.main.repositories import PriceRepositoryInterface

class PriceService:
    def __init__(self, repository: PriceRepositoryInterface):
        self.repository = repository

    def create_price(self, price_data: dict) -> Price:
        price = Price(**price_data)
        return self.repository.add_price(price)

    def get_price(self, price_id: str) -> Optional[Price]:
        return self.repository.get_price(price_id)

    def update_price(self, price_id: str, update_data: dict) -> Optional[Price]:
        return self.repository.update_price(price_id, update_data)

    def delete_price(self, price_id: str) -> bool:
        return self.repository.delete_price(price_id)

    def list_prices(self) -> List[Price]:
        return self.repository.list_prices()
