from pydantic import BaseModel, field_validator
from typing import Optional

class Promotion(BaseModel):
    promotion_id: str
    title: str
    description: str
    discount_percentage: float
    duration_days: int

    @field_validator('discount_percentage')
    def validate_discount(cls, v):
        if not 0 <= v <= 100:
            raise ValueError('Discount must be between 0 and 100')
        return v
