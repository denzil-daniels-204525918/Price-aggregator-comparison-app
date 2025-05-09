# src/main/api/product_api.py
from fastapi import APIRouter, HTTPException, Query
from main.repositories.inmemory.inmemory_product_repository import InMemoryProductRepository
from main.services.product_service import ProductService
from main.product import Product

product_repository = InMemoryProductRepository()
product_service = ProductService(product_repository)

router = APIRouter()

@router.post("/products")
async def create_product(product: Product):
    created = product_service.create_product(product.model_dump())
    return created

@router.get("/products/{product_id}")
def get_product(product_id: str):
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/products/{product_id}")
def update_product(product_id: str, name: str = Query(...), description: str = Query(...), category: str = Query(...)):
    updated = product_service.update_product(product_id, {
        "name": name,
        "description": description,
        "category": category
    })
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
    return product_service.list_products()
