# src/repositories/promotion_repository.py

from abc import ABC, abstractmethod
from typing import List
from price_aggregator.main.models.promotion import Promotion

class PromotionRepository(ABC):

    @abstractmethod
    def save(self, promotion: Promotion) -> None:
        pass

    @abstractmethod
    def find_by_id(self, promotion_id: str) -> Promotion:
        pass

    @abstractmethod
    def find_all(self) -> List[Promotion]:
        pass

    @abstractmethod
    def delete(self, promotion_id: str) -> None:
        pass
