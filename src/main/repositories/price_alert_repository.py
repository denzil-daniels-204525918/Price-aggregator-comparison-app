from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List
from price_aggregator.main.models.price_alert import PriceAlert


T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        pass

    @abstractmethod
    def delete(self, id: ID) -> None:
        pass

class PriceAlertRepository(Repository[PriceAlert, str], ABC):
    pass
