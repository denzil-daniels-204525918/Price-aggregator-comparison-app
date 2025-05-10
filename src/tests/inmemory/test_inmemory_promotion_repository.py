# src/tests/inmemory/test_inmemory_promotion_repository.py

import pytest
from src.main.promotion import Promotion
from src.main.repositories.inmemory.inmemory_promotion_repository import InMemoryPromotionRepository

@pytest.fixture
def repository():
    return InMemoryPromotionRepository()

@pytest.fixture
def sample_promotion():
    return Promotion(
        promotion_id="promo123",
        title="Half Price",
        description="50% off all items",
        discount_percentage=50,
        duration_days=7  # ✅ Add this missing required field
    )

def test_save_and_find_by_id(repository, sample_promotion):
    repository.save(sample_promotion)
    result = repository.find_by_id("promo123")
    assert result == sample_promotion

def test_find_all(repository, sample_promotion):
    repository.save(sample_promotion)
    result = repository.find_all()
    assert len(result) == 1

def test_delete(repository, sample_promotion):
    repository.save(sample_promotion)
    repository.delete("promo123")
    result = repository.find_by_id("promo123")
    assert result is None
