# src/main/creational_patterns/abstract_factory/retailer_data_factory.py
from abc import ABC, abstractmethod

class RetailerDataFactory(ABC):

    @abstractmethod
    def create_product(self, product_id, name, price, description):
        pass

    @abstractmethod
    def create_promotion(self, promo_id, description, discount):
        pass

    @abstractmethod
    def create_price_alert(self, alert_id, price_threshold):
        pass
