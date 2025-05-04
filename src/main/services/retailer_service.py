# src/main/services/retailer_service.py

from typing import List, Optional
from main.retailer import Retailer
from main.repositories.retailer_repository import RetailerRepository


class RetailerService:
    def __init__(self, retailer_repository: RetailerRepository):
        self.retailer_repository = retailer_repository

    def add_retailer(self, retailer: Retailer) -> None:
        self.retailer_repository.save(retailer)

    def get_retailer(self, retailer_id: str) -> Optional[Retailer]:
        return self.retailer_repository.find_by_id(retailer_id)

    def get_all_retailers(self) -> List[Retailer]:
        return self.retailer_repository.find_all()

    def delete_retailer(self, retailer_id: str) -> None:
        self.retailer_repository.delete(retailer_id)

    def update_contact_info(self, retailer_id: str, new_contact: str) -> Optional[Retailer]:
        retailer = self.retailer_repository.find_by_id(retailer_id)
        if retailer:
            retailer.contact_info = new_contact
            return self.retailer_repository.update(retailer_id, retailer)
        return None
