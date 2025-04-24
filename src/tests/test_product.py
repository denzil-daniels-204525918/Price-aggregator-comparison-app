# src/tests/test_product.py
import pytest
from src.main.product import Product

def test_product_creation():
    product = Product(product_id="1", name="Apple", price=1.5)
    assert product.product_id == "1"
    assert product.name == "Apple"
    assert product.price == 1.5
