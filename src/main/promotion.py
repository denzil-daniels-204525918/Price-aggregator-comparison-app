# src/main/promotion.py

class Promotion:
    def __init__(self, promotion_id: str, title: str, description: str, discount_percentage: float):
        self.promotion_id = promotion_id
        self.title = title
        self.description = description
        self.discount_percentage = discount_percentage

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.discount_percentage / 100)
