# src/tests/api/test_retailer_api.py
import pytest
from fastapi.testclient import TestClient
from main.app import app

client = TestClient(app)

@pytest.fixture(scope="function")
def create_retailer():
    retailer = {
        "retailer_id": "R999",
        "name": "Test Retailer",
        "contact_info": "test@retailer.com"
    }
    response = client.post("/retailers", json=retailer)
    assert response.status_code == 200
    return response.json()  # Return the actual created retailer data

def test_create_and_get_retailer(create_retailer):
    retailer = create_retailer
    # The retailer is already created by the fixture, no need to create again
    get_response = client.get(f"/retailers/{retailer['retailer_id']}")
    assert get_response.status_code == 200
    assert get_response.json()["retailer_id"] == "R999"
    assert get_response.json()["name"] == "Test Retailer"

def test_update_contact_info(create_retailer):
    retailer = create_retailer
    retailer_id = retailer["retailer_id"]
    contact_info = "new@contact.com"

    response = client.put(f"/retailers/{retailer_id}/contact?contact_info={contact_info}")
    assert response.status_code == 200
    assert response.json()["contact_info"] == contact_info

def test_delete_retailer(create_retailer):
    retailer = create_retailer
    retailer_id = retailer["retailer_id"]

    response = client.delete(f"/retailers/{retailer_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Retailer deleted successfully"

    # Verify the retailer is actually deleted
    get_response = client.get(f"/retailers/{retailer_id}")
    assert get_response.status_code == 404