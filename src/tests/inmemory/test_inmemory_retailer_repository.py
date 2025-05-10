# src/main/repositories/inmemory/inmemory_retailer_repository.py
from typing import Dict, List
from src.main.models.retailer import Retailer

class InMemoryRetailerRepository:
    def __init__(self):
        self.retailers: Dict[str, Retailer] = {}

    def save(self, retailer: Retailer) -> Retailer:
        self.retailers[retailer.retailer_id] = retailer
        return retailer

    def find_by_id(self, retailer_id: str) -> Retailer:
        return self.retailers.get(retailer_id)

    def find_all(self) -> List[Retailer]:
        return list(self.retailers.values())

    def delete(self, retailer_id: str) -> None:
        if retailer_id in self.retailers:
            del self.retailers[retailer_id]