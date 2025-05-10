from main.product import Product
from src.main.creational_patterns.builders.promotion import Promotion
from .price_alert import PriceAlert
from main.creational_patterns.builder.product_report import ProductReport


class ProductReportBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = None
        self._price_history = []
        self._promotion = None
        self._alert = None

    def set_product(self, product: Product):
        self._product = product
        return self

    def add_price_history(self, prices: list):
        if not prices:
            raise ValueError("Price history cannot be empty")
        self._price_history.extend(prices)
        return self

    def set_promotion(self, promotion: Promotion):
        self._promotion = promotion
        return self

    def add_price_alert(self, alert: PriceAlert):
        self._alert = alert
        return self

    def build(self):
        report = ProductReport(
            product=self._product,
            price_history=self._price_history,
            promotion=self._promotion,
            alert=self._alert
        )
        self.reset()  # Reset for next build
        return report
