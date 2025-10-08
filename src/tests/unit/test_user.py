import pytest
from price_aggregator.main.user import User

def test_user_creation():
    user = User(user_id="test123", name="Test User", email="test@example.com")
    assert user.user_id == "test123"
    assert user.name == "Test User"
    assert user.email == "test@example.com"

def test_user_login():
    user = User(user_id="test123", name="Test User", email="test@example.com")
    # Add login test logic here
    assert user.user_id == "test123"