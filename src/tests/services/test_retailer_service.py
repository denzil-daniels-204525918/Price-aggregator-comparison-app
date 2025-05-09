# src/tests/services/test_retailer_service.py

import pytest
from unittest.mock import MagicMock
from main.services.retailer_service import RetailerService
from main.retailer import Retailer


@pytest.fixture
def mock_retailer_repo():
    return MagicMock()

@pytest.fixture
def retailer_service(mock_retailer_repo):
    return RetailerService(mock_retailer_repo)


def test_add_retailer(retailer_service, mock_retailer_repo):
    retailer = Retailer(retailer_id="R101", name="Retailer A", contact_info="contact@reta.com")
    retailer_service.add_retailer(retailer)
    mock_retailer_repo.save.assert_called_once_with(retailer)


def test_get_retailer(retailer_service, mock_retailer_repo):
    retailer = Retailer(retailer_id="R101", name="Retailer A", contact_info="contact@reta.com")
    mock_retailer_repo.find_by_id.return_value = retailer
    result = retailer_service.get_retailer("R101")
    assert result == retailer
    mock_retailer_repo.find_by_id.assert_called_once_with("R101")


def test_get_all_retailers(retailer_service, mock_retailer_repo):
    retailers = [
        Retailer(retailer_id="R101", name="Retailer A", contact_info="contact@reta.com"),
        Retailer(retailer_id="R102", name="Retailer B", contact_info="contact@retb.com")
    ]
    mock_retailer_repo.find_all.return_value = retailers
    result = retailer_service.get_all_retailers()
    assert result == retailers
    mock_retailer_repo.find_all.assert_called_once()


def test_delete_retailer(retailer_service, mock_retailer_repo):
    retailer_service.delete_retailer("R101")
    mock_retailer_repo.delete.assert_called_once_with("R101")


from unittest.mock import call

def test_update_contact_info(retailer_service, mock_retailer_repo):
    retailer = Retailer(retailer_id="R101", name="Retailer A", contact_info="old@email.com")
    updated = Retailer(retailer_id="R101", name="Retailer A", contact_info="new@email.com")

    mock_retailer_repo.find_by_id.return_value = retailer
    mock_retailer_repo.update.return_value = updated
    result = retailer_service.update_contact_info("R101", "new@email.com")

    # Retrieve the actual arguments passed to the update method
    update_call_args = mock_retailer_repo.update.call_args[0]
    actual_updated_retailer = update_call_args[1]  # The second argument is the Retailer object

    # Compare the attributes, ignoring memory addresses
    assert actual_updated_retailer.retailer_id == updated.retailer_id
    assert actual_updated_retailer.name == updated.name
    assert actual_updated_retailer.contact_info == updated.contact_info

