# src/tests/test_inmemory_user_repository.py

import pytest
from src.main.module.module_user import User
from src.main.repositories.inmemory.inmemory_user_repository import InMemoryUserRepository

@pytest.fixture
def user_repository():
    return InMemoryUserRepository()

def test_save_and_find_by_id(user_repository):
    user = User(user_id="u1", name="Alice", email="alice@example.com")
    user_repository.save(user)

    found_user = user_repository.find_by_id("u1")
    assert found_user is not None
    assert found_user.id == "u1"
    assert found_user.name == "Alice"

def test_find_all(user_repository):
    user1 = User(user_id="u1", name="Alice", email="alice@example.com")
    user2 = User(user_id="u2", name="Bob", email="bob@example.com")
    user_repository.save(user1)
    user_repository.save(user2)

    users = user_repository.find_all()
    assert len(users) == 2
    assert user1 in users
    assert user2 in users

def test_delete(user_repository):
    user = User(user_id="u1", name="Alice", email="alice@example.com")
    user_repository.save(user)

    user_repository.delete("u1")
    assert user_repository.find_by_id("u1") is None
