# src/repositories/retailer_repository.py
from .repository import Repository
from src.main.retailer import Retailer

class RetailerRepository(Repository[Retailer, str]):
    pass