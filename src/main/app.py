from fastapi import FastAPI
import uvicorn

from .api.retailer_api import router as retailer_router
from .api.product_api import router as product_router
from .api.price_api import router as price_router

app = FastAPI()

app.include_router(retailer_router)
app.include_router(product_router)
app.include_router(price_router)

def main():
    """CLI entry point for running the FastAPI app."""
    uvicorn.run("main.app:app", host="0.0.0.0", port=8000, reload=True)
