from price_aggregator.main.models.price_alert import PriceAlert, Price  # Added Price import
from typing import List, Optional

class InMemoryPriceAlertRepository:
    def __init__(self):
        self.alerts = []

    def save(self, alert: PriceAlert) -> None:
        self.alerts.append(alert)

    def find_by_id(self, alert_id: str) -> Optional[PriceAlert]:
        return next((alert for alert in self.alerts if alert.alert_id == alert_id), None)

    def find_all(self) -> List[PriceAlert]:
        return self.alerts

    def delete(self, alert_id: str) -> bool:
        alert = self.find_by_id(alert_id)
        if alert:
            self.alerts.remove(alert)
            return True
        return False

class InMemoryPriceRepository:
    def __init__(self):
        self.prices = []

    def save(self, price: Price) -> None:
        self.prices.append(price)

    def find_by_product_id(self, product_id: str) -> List[Price]:
        return [price for price in self.prices if price.product_id == product_id]