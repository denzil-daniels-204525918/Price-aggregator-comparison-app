# src/main/api/retailer_api.py
from fastapi import APIRouter, HTTPException, Query
from main.repositories.inmemory.inmemory_retailer_repository import InMemoryRetailerRepository
from main.services.retailer_service import RetailerService
from main.retailer import Retailer

retailer_repository = InMemoryRetailerRepository()
retailer_service = RetailerService(retailer_repository)

router = APIRouter()

@router.get("/retailers/{retailer_id}")
def get_retailer(retailer_id: str):
    retailer = retailer_service.get_retailer(retailer_id)
    if not retailer:
        raise HTTPException(status_code=404, detail="Retailer not found")
    return retailer

@router.post("/retailers")
async def create_retailer(retailer: Retailer):
    created_retailer = retailer_service.create_retailer(retailer.model_dump())
    return created_retailer

@router.put("/retailers/{retailer_id}/contact")
def update_contact_info(retailer_id: str, contact_info: str = Query(...)):
    updated = retailer_service.update_contact_info(retailer_id, contact_info)
    if not updated:
        raise HTTPException(status_code=404, detail="Retailer not found")
    return updated

@router.delete("/retailers/{retailer_id}")
def delete_retailer(retailer_id: str):
    success = retailer_service.delete_retailer(retailer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Retailer not found")
    return {"detail": "Retailer deleted successfully"}

@router.get("/retailers")
def list_retailers():
    return retailer_service.list_retailers()