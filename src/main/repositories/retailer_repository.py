from .repository import Repository
from price_aggregator.main.models.retailer import Retailer

class RetailerRepository(Repository[Retailer, str]):
    """
    Repository for Retailer entity extending base Repository class.
    """
    pass
