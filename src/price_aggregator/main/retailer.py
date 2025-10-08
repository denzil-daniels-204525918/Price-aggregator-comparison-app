from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

# Create router for retailer endpoints
router = APIRouter(prefix="/retailers", tags=["retailers"])

class Retailer(BaseModel):
    retailer_id: str
    name: str
    contact_info: str
    products: List = []  # Simplified for now

@router.get("/")
async def get_retailers():
    return {"message": "Retailers endpoint"}

@router.post("/")
async def create_retailer(retailer: Retailer):
    return {"message": "Retailer created", "retailer": retailer}