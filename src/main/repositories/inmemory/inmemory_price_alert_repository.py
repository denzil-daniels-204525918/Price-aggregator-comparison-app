# src/main/repositories/inmemory/inmemory_price_alert_repository.py
from typing import Dict, Optional, List
from src.main.price_alert import PriceAlert
from src.main.price_alert import Price


class InMemoryPriceRepository:
    def __init__(self):
        self.prices: Dict[str, Price] = {}

    def add_price(self, price_data: dict) -> Price:
        price = Price(**price_data)
        self.prices[price.price_id] = price
        return price

    def get_price(self, price_id: str) -> Optional[Price]:
        return self.prices.get(price_id)

    def update_price(self, price_id: str, update_data: dict) -> Optional[Price]:
        if price_id in self.prices:
            for key, value in update_data.items():
                setattr(self.prices[price_id], key, value)
            return self.prices[price_id]
        return None

    def delete_price(self, price_id: str) -> bool:
        if price_id in self.prices:
            del self.prices[price_id]
            return True
        return False

    def find_all(self) -> List[Price]:
        return list(self.prices.values())


class InMemoryPriceAlertRepository:
    def __init__(self):
        self.alerts: Dict[str, PriceAlert] = {}

    def save(self, alert: PriceAlert) -> PriceAlert:
        self.alerts[alert.alert_id] = alert
        return alert

    def find_by_id(self, alert_id: str) -> Optional[PriceAlert]:
        return self.alerts.get(alert_id)

    def find_all(self) -> List[PriceAlert]:
        return list(self.alerts.values())

    def delete(self, alert_id: str) -> bool:
        if alert_id in self.alerts:
            del self.alerts[alert_id]
            return True
        return False