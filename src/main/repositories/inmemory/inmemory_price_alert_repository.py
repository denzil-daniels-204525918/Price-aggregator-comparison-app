# src/main/repositories/inmemory/inmemory_price_repository.py
from typing import Dict, Optional

class InMemoryPriceRepository:
    def __init__(self):
        self.prices: Dict[str, dict] = {}

    def add_price(self, price_data: dict) -> dict:
        price_id = price_data["price_id"]
        self.prices[price_id] = price_data
        return price_data

    def get_price(self, price_id: str) -> Optional[dict]:
        return self.prices.get(price_id)

    def update_price(self, price_id: str, update_data: dict) -> Optional[dict]:
        if price_id in self.prices:
            self.prices[price_id].update(update_data)
            return self.prices[price_id]
        return None

    def delete_price(self, price_id: str) -> bool:
        if price_id in self.prices:
            del self.prices[price_id]
            return True
        return False

    def list_prices(self) -> list:
        return list(self.prices.values())
