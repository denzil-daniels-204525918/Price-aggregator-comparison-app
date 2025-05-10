# src/tests/test_promotion.py
import pytest
from src.main.promotion import Promotion
from src.main.product import Product


def test_apply_promotion():
    product = Product(
        product_id="P101",
        name="Product A",
        price=100.00,
        description="Description of Product A"
    )
    promotion = Promotion(
        promotion_id="Promo101",
        title="10% Off Promotion",
        description="10% off",
        discount_percentage=10.00,
        duration_days=7  # Added required field
    )

    # Test applying promotion
    discounted_price = product.price * (1 - promotion.discount_percentage / 100)
    assert discounted_price == 90.00
    assert promotion.discount_percentage == 10.00


def test_promotion_creation():
    promotion = Promotion(
        promotion_id="Promo101",
        title="10% Off Promotion",
        description="10% off",
        discount_percentage=10.00,
        duration_days=7  # Added required field
    )
    assert promotion.promotion_id == "Promo101"
    assert promotion.title == "10% Off Promotion"
    assert promotion.duration_days == 7


def test_promotion_with_invalid_discount():
    with pytest.raises(ValueError):
        Promotion(
            promotion_id="Promo102",
            title="Invalid Promotion",
            description="Invalid discount",
            discount_percentage=-5.00,  # Negative discount
            duration_days=7
        )