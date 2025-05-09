# src/main/repositories/inmemory/inmemory_retailer_repository.py
from typing import Dict, Optional

class InMemoryRetailerRepository:
    def __init__(self):
        self.retailers: Dict[str, dict] = {}

    def add_retailer(self, retailer_data: dict) -> dict:
        retailer_id = retailer_data["retailer_id"]
        self.retailers[retailer_id] = retailer_data
        return retailer_data

    def get_retailer(self, retailer_id: str) -> Optional[dict]:
        return self.retailers.get(retailer_id)

    def update_retailer(self, retailer_id: str, update_data: dict) -> Optional[dict]:
        if retailer_id in self.retailers:
            self.retailers[retailer_id].update(update_data)
            return self.retailers[retailer_id]
        return None

    def delete_retailer(self, retailer_id: str) -> bool:
        if retailer_id in self.retailers:
            del self.retailers[retailer_id]
            return True
        return False

    def list_retailers(self) -> list:
        return list(self.retailers.values())