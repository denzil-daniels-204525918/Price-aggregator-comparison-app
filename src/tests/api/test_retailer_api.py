# src/tests/api/test_retailer_api.py
import pytest
from fastapi.testclient import TestClient
from src.main.app import app

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
    return response.json()

def test_create_and_get_retailer(create_retailer):
    retailer = create_retailer
    response = client.get(f"/retailers/{retailer['retailer_id']}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Retailer"

def test_update_contact_info(create_retailer):
    retailer = create_retailer
    response = client.put(
        f"/retailers/{retailer['retailer_id']}/contact?new_contact=updated@retailer.com"
    )
    assert response.status_code == 200
    assert response.json()["contact_info"] == "updated@retailer.com"

def test_delete_retailer(create_retailer):
    retailer = create_retailer
    response = client.delete(f"/retailers/{retailer['retailer_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Retailer deleted successfully"