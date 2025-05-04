import pytest
from unittest.mock import MagicMock
from main.services.product_service import ProductService
from main.product import Product


@pytest.fixture
def mock_repo():
    return MagicMock()


@pytest.fixture
def product_service(mock_repo):
    return ProductService(mock_repo)


def test_add_product(product_service, mock_repo):
    product = Product(product_id=1, name="Milk", price=10.0, description="Full cream milk", category="Dairy")
    mock_repo.save.return_value = product

    result = product_service.add_product("Milk", "Dairy", "Full cream milk")

    mock_repo.save.assert_called_once()
    assert result.name == "Milk"
    assert result.category == "Dairy"


def test_get_all_products(product_service, mock_repo):
    products = [
        Product(product_id=1, name="Milk", price=10.0, description="Full cream milk", category="Dairy"),
        Product(product_id=2, name="Bread", price=5.0, description="Whole wheat bread", category="Bakery")
    ]
    mock_repo.find_all.return_value = products

    result = product_service.get_all_products()

    mock_repo.find_all.assert_called_once()
    assert len(result) == 2


def test_update_product(product_service, mock_repo):
    # Create an existing product with required fields
    product = Product(product_id=1, name="Milk", price=10.0, description="Old desc", category="Dairy")

    # Mock repository methods
    mock_repo.find_by_id.return_value = product
    mock_repo.update.return_value = product  # Returning the same updated product

    # Call the service method to update the product
    result = product_service.update_product(product.product_id, description="New desc")

    # Ensure the update method is called with the modified product object
    mock_repo.update.assert_called_once_with(product.product_id, product)
    assert result.description == "New desc"


def test_delete_product(product_service, mock_repo):
    mock_repo.delete.return_value = True

    result = product_service.delete_product("some-id")

    mock_repo.delete.assert_called_once_with("some-id")
    assert result
