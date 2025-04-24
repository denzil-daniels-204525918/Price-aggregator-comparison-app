# src/repositories/inmemory/inmemory_promotion_repository.py

from src.main.repositories.promotion_repository import PromotionRepository
from src.main.promotion import Promotion
from typing import Dict, List


class InMemoryPromotionRepository(PromotionRepository):
    def __init__(self):
        self.storage: Dict[str, Promotion] = {}

    def save(self, promotion: Promotion) -> None:
        self.storage[promotion.promotion_id] = promotion

    def find_by_id(self, promotion_id: str) -> Promotion:
        return self.storage.get(promotion_id)

    def find_all(self) -> List[Promotion]:
        return list(self.storage.values())

    def delete(self, promotion_id: str) -> None:
        self.storage.pop(promotion_id, None)
