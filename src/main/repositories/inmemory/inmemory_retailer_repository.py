from typing import Dict, Optional, List
from src.main.models.retailer import Retailer

class InMemoryRetailerRepository:
    def __init__(self):
        self.retailers: Dict[str, Retailer] = {}

    def save(self, retailer: Retailer) -> Retailer:
        self.retailers[retailer.retailer_id] = retailer
        return retailer

    def find_by_id(self, retailer_id: str) -> Optional[Retailer]:
        return self.retailers.get(retailer_id)

    def find_all(self) -> List[Retailer]:
        return list(self.retailers.values())

    def delete(self, retailer_id: str) -> bool:
        if retailer_id in self.retailers:
            del self.retailers[retailer_id]
            return True
        return False

    def update(self, retailer_id: str, retailer: Retailer) -> Retailer:
        if retailer_id in self.retailers:
            self.retailers[retailer_id] = retailer
            return retailer
        raise ValueError("Retailer not found")
