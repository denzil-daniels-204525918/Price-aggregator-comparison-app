from typing import Optional, List
from src.main.price_alert import PriceAlert
from src.main.repositories.price_alert_repository import PriceAlertRepository

class InMemoryPriceAlertRepository(PriceAlertRepository):
    def __init__(self):
        self._storage = {}

    def save(self, alert: PriceAlert) -> None:
        self._storage[alert.alert_id] = alert  # Change 'id' to 'alert_id'

    def find_by_id(self, id: str) -> Optional[PriceAlert]:
        return self._storage.get(id)

    def find_all(self) -> List[PriceAlert]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
