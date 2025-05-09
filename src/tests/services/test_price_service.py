from main.product import Product
from main.services.price_service import PriceService
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def price_service(mock_repo):
    return PriceService(mock_repo)

def test_update_product_price(price_service, mock_repo):
    product = Product(product_id="1", name="Milk", price=10.0, category="Dairy", description="Full cream milk")
    updated_product = Product(product_id="1", name="Milk", price=12.0, category="Dairy", description="Full cream milk")

    mock_repo.find_by_id.return_value = product
    mock_repo.update_price.return_value = updated_product  # ✅ THIS LINE IS ESSENTIAL

    result = price_service.update_price("1", 12.0)

    assert result.price == 12.0
    mock_repo.update_price.assert_called_once_with("1", 12.0)
