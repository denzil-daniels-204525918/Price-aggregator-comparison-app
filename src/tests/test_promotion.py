import unittest
from src.main.promotion import Promotion
from src.main.product import Product

class TestPromotion(unittest.TestCase):
    def test_promotion_creation(self):
        promotion = Promotion(promotion_id="Promo101", description="10% off", discount=10.00)
        self.assertEqual(promotion.promotion_id, "Promo101")
        self.assertEqual(promotion.description, "10% off")
        self.assertEqual(promotion.discount, 10.00)

    def test_apply_promotion(self):
        product = Product(product_id="P101", name="Product A", price=100.00, description="Description of Product A")
        promotion = Promotion(promotion_id="Promo101", description="10% off", discount=10.00)
        promotion.apply_promotion(product)
        self.assertEqual(product.price, 90.00)  # After applying the promotion, the price should be reduced by 10%

if __name__ == '__main__':
    unittest.main()
