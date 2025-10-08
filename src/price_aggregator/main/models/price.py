# --- src/main/models/price.py ---
from pydantic import BaseModel

class Price(BaseModel):
    price_id: str
    product_id: str
    retailer_id: str
    amount: float
    currency: str
    date: str  # ISO format (e.g., '2025-05-04')
    alert_id: str
    price_threshold: float
