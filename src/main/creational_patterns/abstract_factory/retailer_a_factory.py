from .retailer_data_factory import RetailerDataFactory
from .product import Product
from src.main.creational_patterns.abstract_factory.promotion import Promotion
from .price_alert import PriceAlert


class RetailerAFactory(RetailerDataFactory):
    def create_product(self, product_id, name, price, description):
        return Product(product_id=f"A-{product_id}", name=name, price=price, description=description)

    def create_promotion(self, name, discount):
        return Promotion(name=name, discount=discount)


    def create_price_alert(self, alert_id, threshold_price):
        return PriceAlert(f"A-{alert_id}", threshold_price, is_active=True)



