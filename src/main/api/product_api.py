from fastapi import APIRouter, HTTPException, Query
from src.main.repositories.inmemory.inmemory_product_repository import InMemoryProductRepository
from src.main.services.product_service import ProductService
from src.main.product import Product

product_repository = InMemoryProductRepository()
product_service = ProductService(product_repository)

router = APIRouter()

@router.post("/products")
async def create_product(product: Product):
    created_product = product_service.create_product(product.model_dump())
    return created_product

@router.get("/products/{product_id}")
def get_product(product_id: str):
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}")
def update_product(
        product_id: str,
        name: str = Query(None),
        description: str = Query(None),
        category: str = Query(None),
        price: float = Query(None)
):
    update_data = {}
    if name: update_data["name"] = name
    if description: update_data["description"] = description
    if category: update_data["category"] = category
    if price is not None: update_data["price"] = price

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    updated = product_service.update_product(product_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/products/{product_id}")
def delete_product(product_id: str):
    success = product_service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}

@router.get("/products")
def list_products():
    return product_service.get_all_products()
