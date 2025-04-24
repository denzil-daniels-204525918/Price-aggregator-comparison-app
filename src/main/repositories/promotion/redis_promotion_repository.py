# Stub or actual Redis implementation


import redis

from src.main.promotion import Promotion
from src.main.repositories.promotion_repository import PromotionRepository
from typing import List

class RedisPromotionRepositoryStub(PromotionRepository):
    def __init__(self):
        self._redis = {}  # Simulating a Redis database with a dictionary

    def save(self, promotion: Promotion) -> None:
        self._redis[promotion.promotion_id] = promotion

    def find_by_id(self, promotion_id: str) -> Promotion:
        return self._redis.get(promotion_id, None)

    def find_all(self) -> List[Promotion]:
        return list(self._redis.values())

    def delete(self, promotion_id: str) -> None:
        if promotion_id in self._redis:
            del self._redis[promotion_id]
