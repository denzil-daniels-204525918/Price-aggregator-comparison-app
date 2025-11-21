from price_aggregator.main.models.promotion import Promotion
from price_aggregator.main.repositories.promotion_repository import PromotionRepository
from typing import List

class RedisPromotionRepositoryStub(PromotionRepository):
    def __init__(self):
        self._redis = {}  # Simulating a Redis database with a dictionary

    def save(self, promotion: Promotion) -> None:
        print(f"Saving promotion to Redis: {promotion.promotion_id}")  # Added logging for debugging
        self._redis[promotion.promotion_id] = promotion  # Storing promotion by its ID

    def find_by_id(self, promotion_id: str) -> Promotion:
        print(f"Finding promotion in Redis by ID: {promotion_id}")  # Added logging
        return self._redis.get(promotion_id, None)  # Return promotion or None if not found

    def find_all(self) -> List[Promotion]:
        return list(self._redis.values())  # Return all promotions in Redis

    def delete(self, promotion_id: str) -> None:
        print(f"Deleting promotion from Redis: {promotion_id}")  # Added logging
        if promotion_id in self._redis:
            del self._redis[promotion_id]  # Delete the promotion if it exists
