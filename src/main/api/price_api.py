from fastapi import APIRouter, HTTPException, Query
from src.main.repositories.inmemory.inmemory_price_alert_repository import InMemoryPriceRepository
from src.main.services.price_service import PriceService
from src.main.price_alert import Price

price_repository = InMemoryPriceRepository()
price_service = PriceService(price_repository)

router = APIRouter()

@router.post("/prices")
async def create_price(price: Price):
    created = price_service.create_price(price.model_dump())
    return created

@router.get("/prices/{price_id}")
def get_price(price_id: str):
    price = price_service.get_price(price_id)
    if not price:
        raise HTTPException(status_code=404, detail="Price not found")
    return price

@router.put("/prices/{price_id}")
def update_price(
        price_id: str,
        amount: float = Query(...),
        currency: str = Query(...),
        date: str = Query(...)
):
    updated = price_service.update_price(price_id, {
        "amount": amount,
        "currency": currency,
        "date": date
    })
    if not updated:
        raise HTTPException(status_code=404, detail="Price not found")
    return updated

@router.delete("/prices/{price_id}")
def delete_price(price_id: str):
    success = price_service.delete_price(price_id)
    if not success:
        raise HTTPException(status_code=404, detail="Price not found")
    return {"detail": "Price deleted successfully"}

@router.get("/prices")
def list_prices():
    return price_service.list_prices()
