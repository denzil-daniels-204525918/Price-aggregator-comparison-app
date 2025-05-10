# src/tests/inmemory/test_inmemory_product_repository.py
from src.main.product import Product
from src.main.repositories.inmemory.inmemory_product_repository import InMemoryProductRepository

def test_find_by_id():
    repo = InMemoryProductRepository()
    product = Product(product_id="1", name="Apple", price=1.0)
    repo.save(product)

    result = repo.find_by_id("1")
    assert result == product
