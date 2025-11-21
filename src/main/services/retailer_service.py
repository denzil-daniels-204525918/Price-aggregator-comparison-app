# --- src/main/services/retailer_service.py ---
from typing import Optional, List
from price_aggregator.main.models.retailer import Retailer
from price_aggregator.main.repositories.inmemory.inmemory_retailer_repository import InMemoryRetailerRepository

class RetailerService:
    def __init__(self, repository: Optional[InMemoryRetailerRepository] = None):
        self.repository = repository or InMemoryRetailerRepository()

    def create_retailer(self, retailer_data: dict) -> Retailer:
        retailer = Retailer(**retailer_data)
        return self.repository.save(retailer)

    def get_retailer(self, retailer_id: str) -> Optional[Retailer]:
        return self.repository.find_by_id(retailer_id)

    def get_all_retailers(self) -> List[Retailer]:
        return self.repository.find_all()

    def delete_retailer(self, retailer_id: str) -> bool:
        return self.repository.delete(retailer_id)

    def update_contact_info(self, retailer_id: str, new_contact: str) -> Optional[Retailer]:
        retailer = self.repository.find_by_id(retailer_id)
        if not retailer:
            return None
        retailer.contact_info = new_contact
        return self.repository.save(retailer)

    def update_retailer(self, retailer_id: str, updated_data: dict) -> Optional[Retailer]:
        retailer = self.repository.find_by_id(retailer_id)
        if not retailer:
            return None
        for key, value in updated_data.items():
            if hasattr(retailer, key):
                setattr(retailer, key, value)
        return self.repository.save(retailer)

    def list_retailers(self) -> List[Retailer]:
        return self.repository.find_all()