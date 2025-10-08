import pytest
from price_aggregator.main.product import Product

def test_product_creation():
    product = Product(
        product_id="prod123",
        name="Test Product",
        price=10.99,
        description="Test description"
    )
    assert product.product_id == "prod123"
    assert product.name == "Test Product"
    assert product.price == 10.99