import pytest
from src.main.creational_patterns.simple_factory.product_factory import ProductFactory

def test_create_invalid_product_type():
    with pytest.raises(ValueError):
        ProductFactory.create_product("999", "Mystery Box", 0.99, "Unknown item", "unknown")
