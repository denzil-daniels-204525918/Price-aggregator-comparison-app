from fastapi import APIRouter
from pydantic import BaseModel

# Create router for product endpoints
router = APIRouter(prefix="/products", tags=["products"])

class Product(BaseModel):
    product_id: str
    name: str
    price: float
    description: str

@router.get("/")
async def get_products():
    return {"message": "Products endpoint"}

@router.post("/")
async def create_product(product: Product):
    return {"message": "Product created", "product": product}