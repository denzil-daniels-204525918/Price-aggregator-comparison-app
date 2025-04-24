# src/repositories/saved_list_repository.py
from .repository import Repository
from src.main.saved_list import SavedList

class SavedListRepository(Repository[SavedList, str]):
    pass