from src.main.repositories.promotion_repository import PromotionRepository
from src.main.promotion import Promotion
from typing import Dict, List


class InMemoryPromotionRepository(PromotionRepository):
    def __init__(self):
        self.storage: Dict[str, Promotion] = {}

    def save(self, promotion: Promotion) -> None:
        print(f"Saving promotion: {promotion.promotion_id}")  # Added logging
        self.storage[promotion.promotion_id] = promotion

    def find_by_id(self, promotion_id: str) -> Promotion:
        print(f"Finding promotion by id: {promotion_id}")  # Added logging
        return self.storage.get(promotion_id)

    def find_all(self) -> List[Promotion]:
        return list(self.storage.values())

    def delete(self, promotion_id: str) -> None:
        print(f"Deleting promotion: {promotion_id}")  # Added logging
        self.storage.pop(promotion_id, None)
