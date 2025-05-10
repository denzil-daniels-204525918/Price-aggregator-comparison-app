from .repository import Repository
from src.main.models.retailer import Retailer

class RetailerRepository(Repository[Retailer, str]):
    """
    Repository for Retailer entity extending base Repository class.
    """
    pass
