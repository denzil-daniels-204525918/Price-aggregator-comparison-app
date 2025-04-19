# src/main/promotion.py

class Promotion:
    def __init__(self, promotion_id, description, discount):
        self.promotion_id = promotion_id
        self.description = description
        self.discount = discount  # e.g. 10 means 10%

    def apply_promotion(self, product):
        """
        Applies a percentage discount to a Product instance's price.
        """
        original_price = product.price
        discounted_price = original_price - (original_price * (self.discount / 100))
        product.price = round(discounted_price, 2)
        product.promotion = self.description


    def __str__(self):
        return f"Promotion ID: {self.promotion_id}, Description: {self.description}, Discount: {self.discount}%"
