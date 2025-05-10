# src/tests/api/test_price_api.py
import pytest
from fastapi.testclient import TestClient
from src.main.app import app

client = TestClient(app)

@pytest.fixture(scope="function")
def create_price():
    price = {
        "price_id": "PR001",
        "product_id": "P123",
        "retailer_id": "R999",
        "amount": 49.99,
        "currency": "ZAR",
        "date": "2025-05-04"
    }
    response = client.post("/prices", json=price)
    assert response.status_code == 200
    return response.json()

def test_create_and_get_price(create_price):
    price = create_price
    response = client.get(f"/prices/{price['price_id']}")
    assert response.status_code == 200
    assert response.json()["amount"] == 49.99

def test_update_price(create_price):
    price = create_price
    response = client.put(
        f"/prices/{price['price_id']}?amount=59.99&currency=ZAR&date=2025-06-01"
    )
    assert response.status_code == 200
    assert response.json()["amount"] == 59.99

def test_delete_price(create_price):
    price = create_price
    response = client.delete(f"/prices/{price['price_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Price deleted successfully"