# src/promotion.py

class Promotion:
    def __init__(self, promotion_id: str, description: str, discount: float):
        self.promotion_id = promotion_id
        self.description = description
        self.discount = discount

    def apply_promotion(self, product):
        # Logic to apply the promotion to a product
        if product.price > 0:
            original_price = product.price
            product.price -= (product.price * self.discount / 100)
            print(f"Promotion {self.promotion_id} applied: {original_price} -> {product.price}")
        else:
            print("Product price is invalid, promotion not applied.")
