from abc import ABC, abstractmethod

class RetailerDataFactory(ABC):
    @abstractmethod
    def create_product(self, product_id, name, price, description):
        pass

    @abstractmethod
    def create_promotion(self, name, discount):
        pass

    @abstractmethod
    def create_price_alert(self, alert_id, threshold_price):
        pass
