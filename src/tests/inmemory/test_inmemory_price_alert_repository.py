import pytest
from src.main.price_alert import PriceAlert
from src.main.repositories.inmemory.inmemory_price_alert_repository import InMemoryPriceAlertRepository

@pytest.fixture
def repository():
    return InMemoryPriceAlertRepository()
@pytest.fixture
def sample_alert():
    return PriceAlert(alert_id="a1", price_threshold=10.00)

def test_save_and_find_by_id(repository, sample_alert):
    repository.save(sample_alert)
    found = repository.find_by_id("a1")
    assert found is not None
    assert found.alert_id == "a1"  # Check the 'alert_id' instead of 'product_id'
    assert found.price_threshold == 10.00  # Check the 'price_threshold' instead of 'product_id'

def test_find_all(repository, sample_alert):
    repository.save(sample_alert)
    alerts = repository.find_all()
    assert len(alerts) == 1

def test_delete(repository, sample_alert):
    repository.save(sample_alert)
    repository.delete("a1")
    assert repository.find_by_id("a1") is None
