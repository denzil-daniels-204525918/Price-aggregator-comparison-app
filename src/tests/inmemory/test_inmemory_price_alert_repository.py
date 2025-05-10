# src/main/repositories/inmemory/inmemory_price_alert_repository.py
from typing import Dict, List
from src.main.price_alert import PriceAlert

class InMemoryPriceAlertRepository:
    def __init__(self):
        self.alerts: Dict[str, PriceAlert] = {}

    def save(self, alert: PriceAlert) -> PriceAlert:
        self.alerts[alert.alert_id] = alert
        return alert

    def find_by_id(self, alert_id: str) -> PriceAlert:
        return self.alerts.get(alert_id)

    def find_all(self) -> List[PriceAlert]:
        return list(self.alerts.values())

    def delete(self, alert_id: str) -> None:
        if alert_id in self.alerts:
            del self.alerts[alert_id]