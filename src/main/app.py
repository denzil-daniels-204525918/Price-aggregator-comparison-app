from fastapi import FastAPI
from price_aggregator.main.user import router as user_router
from price_aggregator.main.product import router as product_router
from price_aggregator.main.retailer import router as retailer_router

# Import API routers
try:
    from price_aggregator.main.api.price_api import router as price_router
except ImportError:
    # Create a placeholder if the module doesn't exist
    from fastapi import APIRouter
    price_router = APIRouter(prefix="/prices", tags=["prices"])

try:
    from price_aggregator.main.api.product_api import router as product_api_router
except ImportError:
    from fastapi import APIRouter
    product_api_router = APIRouter(prefix="/api/products", tags=["products-api"])

try:
    from price_aggregator.main.api.retailer_api import router as retailer_api_router
except ImportError:
    from fastapi import APIRouter
    retailer_api_router = APIRouter(prefix="/api/retailers", tags=["retailers-api"])

def main():
    app = FastAPI(
        title="Price Aggregator API",
        description="A price aggregator and comparison system",
        version="0.1.0"
    )

    # Include routers
    app.include_router(user_router)
    app.include_router(product_router)
    app.include_router(retailer_router)
    app.include_router(price_router)
    app.include_router(product_api_router)
    app.include_router(retailer_api_router)

    return app

# For running directly
if __name__ == "__main__":
    import uvicorn
    app = main()
    uvicorn.run(app, host="0.0.0.0", port=8000)