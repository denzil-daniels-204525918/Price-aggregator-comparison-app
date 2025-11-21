from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Price(BaseModel):
    """Represents a price entry for a product"""
    product_id: str
    retailer_id: str
    price: float
    currency: str = "ZAR"
    timestamp: datetime = datetime.now()

class PriceAlert(BaseModel):
    """Represents a price alert set by a user"""
    alert_id: str
    user_id: str
    product_id: str
    target_price: float
    is_active: bool = True
    created_at: datetime = datetime.now()

    def check_trigger(self, current_price: float) -> bool:
        """Check if the current price triggers the alert"""
        return current_price <= self.target_price

    def deactivate(self):
        """Deactivate the price alert"""
        self.is_active = False