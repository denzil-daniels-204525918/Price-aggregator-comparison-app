# src/tests/test_inmemory_product_repository.py

import pytest
from src.main.product import Product
from src.main.repositories.inmemory.inmemory_product_repository import InMemoryProductRepository

@pytest.fixture
def repository():
    return InMemoryProductRepository()

@pytest.fixture
def sample_product():
    return Product(product_id="p1", name="Milk", price=24.99, description="Dairy product")

# src/tests/test_inmemory_product_repository.py
def test_save_and_find_by_id(repository, sample_product):
    repository.save(sample_product)
    found = repository.find_by_id(sample_product.product_id)
    assert found is not None
    assert found.product_id == sample_product.product_id  # Use product_id


def test_find_all(repository, sample_product):
    repository.save(sample_product)
    all_products = repository.find_all()
    assert len(all_products) == 1
    assert all_products[0].product_id == "p1"

def test_delete(repository, sample_product):
    repository.save(sample_product)
    repository.delete("p1")
    assert repository.find_by_id("p1") is None
