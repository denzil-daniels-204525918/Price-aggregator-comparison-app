from fastapi import APIRouter

router = APIRouter(prefix="/api/products", tags=["products-api"])

@router.get("/")
async def get_products():
    return {"message": "Products API endpoint"}