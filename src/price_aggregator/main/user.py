from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

# Create router for user endpoints
router = APIRouter(prefix="/users", tags=["users"])

class User(BaseModel):
    user_id: str
    name: str
    email: str
    password: Optional[str] = None

@router.get("/")
async def get_users():
    return {"message": "Users endpoint"}

@router.post("/")
async def create_user(user: User):
    return {"message": "User created", "user": user}