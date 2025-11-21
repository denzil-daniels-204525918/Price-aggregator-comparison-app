# src/repositories/saved_list_repository.py
from .repository import Repository
from price_aggregator.main.models.saved_list import SavedList

class SavedListRepository(Repository[SavedList, str]):
    pass