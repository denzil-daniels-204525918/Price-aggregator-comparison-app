from src.main.promotion import Promotion
from src.main.repositories.promotion_repository import PromotionRepository
from typing import List

class FileSystemPromotionRepositoryStub(PromotionRepository):
    def __init__(self):
        self._storage = []  # Simulating a file with an in-memory list

    def save(self, promotion: Promotion) -> None:
        self._storage.append(promotion)

    def find_by_id(self, promotion_id: str) -> Promotion:
        for promo in self._storage:
            if promo.promotion_id == promotion_id:
                return promo
        return None

    def find_all(self) -> List[Promotion]:
        return self._storage

    def delete(self, promotion_id: str) -> None:
        self._storage = [promo for promo in self._storage if promo.promotion_id != promotion_id]
