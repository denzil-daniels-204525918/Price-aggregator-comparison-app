# src/tests/services/test_retailer_service.py

import pytest
from unittest.mock import MagicMock
from src.main.models.retailer import Retailer
from src.main.services.retailer_service import RetailerService

@pytest.fixture
def mock_retailer_repo():
    return MagicMock()

@pytest.fixture
def retailer_service(mock_retailer_repo):
    return RetailerService(repository=mock_retailer_repo)

def test_update_contact_info(retailer_service, mock_retailer_repo):
    # Arrange: Existing retailer and expected updated version
    retailer = Retailer(retailer_id="R101", name="Retailer A", contact_info="old@email.com", products=[])
    updated = Retailer(retailer_id="R101", name="Retailer A", contact_info="new@email.com", products=[])

    # Mock the repository behavior
    mock_retailer_repo.find_by_id.return_value = retailer
    mock_retailer_repo.save.return_value = updated

    # Act: Call the service method
    result = retailer_service.update_contact_info("R101", "new@email.com")

    # Assert: Check that the contact info was updated and save was called
    assert result.contact_info == "new@email.com"
    mock_retailer_repo.find_by_id.assert_called_once_with("R101")
    mock_retailer_repo.save.assert_called_once_with(retailer)
