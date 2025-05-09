from fastapi import FastAPI
from .api.retailer_api import router as retailer_router
from .api.product_api import router as product_router
from .api.price_api import router as price_router



app = FastAPI()

app.include_router(retailer_router)
app.include_router(product_router)
app.include_router(price_router)