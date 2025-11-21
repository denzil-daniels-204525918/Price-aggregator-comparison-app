from fastapi import APIRouter

router = APIRouter(prefix="/api/retailers", tags=["retailers-api"])

@router.get("/")
async def get_retailers():
    return {"message": "Retailers API endpoint"}