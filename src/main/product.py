from pydantic import BaseModel
from typing import Optional
import copy

class Product(BaseModel):
    product_id: str
    name: str
    price: float
    description: Optional[str] = None
    category: Optional[str] = None

    def clone(self):
        return copy.deepcopy(self)