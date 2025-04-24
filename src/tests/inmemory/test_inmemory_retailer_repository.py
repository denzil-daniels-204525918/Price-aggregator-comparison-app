import pytest
from src.main.repositories.inmemory.inmemory_retailer_repository import InMemoryRetailerRepository
from src.main.retailer import Retailer

@pytest.fixture
def retailer_repository():
    return InMemoryRetailerRepository()

def test_save_and_find_by_id(retailer_repository):
    r = Retailer(retailer_id="r1", name="Checkers", contact_info="Cape Town")
    retailer_repository.save(r)

    found = retailer_repository.find_by_id("r1")
    assert found is not None
    assert found.retailer_id == "r1"  # Change from `found.id` to `found.retailer_id`
    assert found.name == "Checkers"

def test_find_all(retailer_repository):
    r1 = Retailer(retailer_id="r1", name="Checkers", contact_info="Cape Town")
    r2 = Retailer(retailer_id="r2", name="Pick n Pay", contact_info="Joburg")
    retailer_repository.save(r1)
    retailer_repository.save(r2)

    retailers = retailer_repository.find_all()
    assert len(retailers) == 2

def test_delete(retailer_repository):
    r = Retailer(retailer_id="r1", name="Checkers", contact_info="Cape Town")
    retailer_repository.save(r)
    retailer_repository.delete("r1")

    assert retailer_repository.find_by_id("r1") is None
