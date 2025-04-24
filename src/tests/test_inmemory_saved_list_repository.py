# src/tests/test_inmemory_saved_list_repository.py

import pytest
from src.main.module.module_saved_list import SavedList
from src.main.repositories.inmemory.inmemory_saved_list_repository import InMemorySavedListRepository

@pytest.fixture
def saved_list_repository():
    return InMemorySavedListRepository()

def test_save_and_find_by_id(saved_list_repository):
    saved = SavedList(saved_list_id="sl1", user_id="u1", name="Weekly Deals", items=["p1", "p2"])
    saved_list_repository.save(saved)

    found = saved_list_repository.find_by_id("sl1")
    assert found is not None
    assert found.id == "sl1"
    assert found.name == "Weekly Deals"

def test_find_all(saved_list_repository):
    s1 = SavedList(saved_list_id="sl1", user_id="u1", name="Weekly Deals", items=["p1"])
    s2 = SavedList(saved_list_id="sl2", user_id="u2", name="Favorites", items=["p3", "p4"])
    saved_list_repository.save(s1)
    saved_list_repository.save(s2)

    lists = saved_list_repository.find_all()
    assert len(lists) == 2
    assert s1 in lists
    assert s2 in lists

def test_delete(saved_list_repository):
    s = SavedList(saved_list_id="sl1", user_id="u1", name="Weekly Deals", items=["p1"])
    saved_list_repository.save(s)

    saved_list_repository.delete("sl1")
    assert saved_list_repository.find_by_id("sl1") is None
