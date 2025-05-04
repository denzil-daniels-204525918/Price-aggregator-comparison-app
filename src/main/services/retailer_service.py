# src/main/services/retailer_service.py
class RetailerService:
    def __init__(self, repository):
        self.repository = repository

    def create_retailer(self, retailer_data):
        return self.repository.add_retailer(retailer_data)

    def get_retailer(self, retailer_id):
        return self.repository.get_retailer(retailer_id)

    def update_contact_info(self, retailer_id, contact_info):
        return self.repository.update_retailer(
            retailer_id,
            {"contact_info": contact_info}
        )

    def delete_retailer(self, retailer_id):
        return self.repository.delete_retailer(retailer_id)

    def list_retailers(self):
        return self.repository.list_retailers()