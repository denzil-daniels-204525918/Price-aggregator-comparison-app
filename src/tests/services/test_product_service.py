# src/tests/services/test_product_service.py
import pytest
from unittest.mock import MagicMock
from src.main.services.product_service import ProductService
from src.main.product import Product

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def product_service(mock_repo):
    return ProductService(mock_repo)

def test_create_product(product_service, mock_repo):
    product_data = {
        "product_id": "1",
        "name": "Milk",
        "price": 10.0,
        "description": "Full cream milk",
        "category": "Dairy"
    }
    expected_product = Product(**product_data)
    mock_repo.save.return_value = expected_product

    result = product_service.create_product(product_data)

    mock_repo.save.assert_called_once()
    assert result.name == "Milk"
    assert result.category == "Dairy"

def test_update_product(product_service, mock_repo):
    existing_product = Product(product_id="1", name="Milk", price=10.0, description="Old desc", category="Dairy")
    updated_data = {"description": "New desc"}

    mock_repo.find_by_id.return_value = existing_product
    updated_product = Product(product_id="1", name="Milk", price=10.0, description="New desc", category="Dairy")
    mock_repo.update.return_value = updated_product

    result = product_service.update_product("1", updated_data)

    mock_repo.update.assert_called_once()
    assert result.description == "New desc"
