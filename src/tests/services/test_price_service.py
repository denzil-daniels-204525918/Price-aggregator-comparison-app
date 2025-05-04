import pytest
from unittest.mock import MagicMock, ANY
from main.services.price_service import PriceService
from main.repositories.product_repository import ProductRepository
from main.product import Product

# Fixture for price_service
@pytest.fixture
def price_service(mock_repo):
    return PriceService(mock_repo)

# Fixture for mock_repo (mocking the ProductRepository)
@pytest.fixture
def mock_repo():
    return MagicMock(spec=ProductRepository)

def test_update_product_price(price_service, mock_repo):
    # Arrange
    product = Product(product_id="1", name="Milk", price=10.0, category="Dairy", description="Full cream milk")
    updated_product = Product(product_id="1", name="Milk", price=12.0, category="Dairy", description="Full cream milk")

    # Mock the repository's find_by_id method
    mock_repo.find_by_id.return_value = product

    # Mock the repository's update method
    mock_repo.update.return_value = updated_product  # Use the same updated_product here

    # Act
    result = price_service.update_product_price("1", 12.0)  # Using product_id and new price

    # Assert
    mock_repo.update.assert_called_once_with("1", ANY)  # Match any instance of Product
    assert result == updated_product  # Ensure the result matches the updated product
