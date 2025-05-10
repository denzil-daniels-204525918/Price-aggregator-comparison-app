# src/tests/test_product.py

import pytest

from src.main.product import Product

# Example test update
def test_product_creation():
    product = Product(
        product_id="1",
        name="Apple",
        price=1.5,
        description="Test description"  # Now required
    )
    assert product.name == "Apple"