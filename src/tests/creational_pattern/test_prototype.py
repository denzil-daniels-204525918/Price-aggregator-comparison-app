import pytest
from src.main.product import Product
def test_clone_product():
    original_product = Product(product_id="301", name="Sugar", price=2.99, description="1kg white sugar")
    cloned_product = original_product.clone()

    # Ensure the cloned product has the same attributes as the original
    assert original_product.product_id == cloned_product.product_id
    assert original_product.name == cloned_product.name
    assert original_product.price == cloned_product.price
    assert original_product.description == cloned_product.description

    # Ensure that the clone is a different object in memory
    assert original_product is not cloned_product

def test_clone_with_modifications():
    original_product = Product(product_id="302", name="Flour", price=1.50, description="1kg all-purpose flour")
    cloned_product = original_product.clone()

    # Modify the cloned product's price
    cloned_product.price = 1.75

    # Ensure that the original product is not affected by the modification
    assert original_product.price == 1.50
    assert cloned_product.price == 1.75
