# src/tests/api/test_product_api.py
import pytest
from fastapi.testclient import TestClient
from main.app import app

client = TestClient(app)

@pytest.fixture(scope="function")
def create_product():
    product = {
        "product_id": "P123",
        "name": "Test Product",
        "description": "Test Description",
        "category": "Test Category"
    }
    response = client.post("/products", json=product)
    assert response.status_code == 200
    return response.json()

def test_create_and_get_product(create_product):
    product = create_product
    response = client.get(f"/products/{product['product_id']}")
    assert response.status_code == 200
    assert response.json()["product_id"] == "P123"

def test_update_product(create_product):
    product = create_product
    response = client.put(
        f"/products/{product['product_id']}?name=Updated&description=Updated%20desc&category=UpdatedCat"
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated"

def test_delete_product(create_product):
    product = create_product
    response = client.delete(f"/products/{product['product_id']}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Product deleted successfully"
