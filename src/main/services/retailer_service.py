# main/services/retailer_service.py
from main.retailer import Retailer

class RetailerService:
    def __init__(self, repository):
        self.repository = repository

    def add_retailer(self, retailer: Retailer) -> Retailer:
        self.repository.save(retailer)
        return retailer

    def get_retailer(self, retailer_id: str) -> Retailer:
        return self.repository.find_by_id(retailer_id)

    def get_all_retailers(self) -> list:
        return self.repository.find_all()

    def delete_retailer(self, retailer_id: str) -> bool:
        return self.repository.delete(retailer_id)

    def update_contact_info(self, retailer_id: str, new_contact_info: str) -> Retailer:
        retailer = self.repository.find_by_id(retailer_id)
        retailer.contact_info = new_contact_info
        self.repository.update(retailer_id, retailer)
        return retailer
