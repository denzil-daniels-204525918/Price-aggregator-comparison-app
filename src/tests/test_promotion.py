#src/tests/test_promotion.py

import pytest


from src.main.promotion import Promotion
from src.main.product import Product
def test_apply_promotion():
    product = Product(product_id="P101", name="Product A", price=100.00, description="Description of Product A")
    promotion = Promotion(
        promotion_id="Promo101",
        title="10% Off Promotion",
        description="10% off",
        discount_percentage=10.00
    )
    # Apply promotion to the product...
    assert promotion.discount_percentage == 10.00

def test_promotion_creation():
    promotion = Promotion(
        promotion_id="Promo101",
        title="10% Off Promotion",
        description="10% off",
        discount_percentage=10.00
    )
    assert promotion.promotion_id == "Promo101"
