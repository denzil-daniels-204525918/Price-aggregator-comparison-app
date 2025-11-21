# Stub or actual database implementation

from price_aggregator.main.models.promotion import Promotion
from price_aggregator.main.repositories.promotion_repository import PromotionRepository
from typing import List

class DatabasePromotionRepositoryStub(PromotionRepository):
    def __init__(self):
        self._db = []  # Simulating a database with an in-memory list

    def save(self, promotion: Promotion) -> None:
        self._db.append(promotion)

    def find_by_id(self, promotion_id: str) -> Promotion:
        for promo in self._db:
            if promo.promotion_id == promotion_id:
                return promo
        return None

    def find_all(self) -> List[Promotion]:
        return self._db

    def delete(self, promotion_id: str) -> None:
        self._db = [promo for promo in self._db if promo.promotion_id != promotion_id]
