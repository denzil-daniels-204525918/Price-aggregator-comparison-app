from fastapi import APIRouter

router = APIRouter(prefix="/prices", tags=["prices"])

@router.get("/")
async def get_prices():
    return {"message": "Prices endpoint"}

@router.get("/compare")
async def compare_prices():
    return {"message": "Price comparison endpoint"}