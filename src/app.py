# src/main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Product(BaseModel):
    id: str
    name: str
    category: str
    description: str

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    return Product(
        id=product_id,
        name="Milk",
        category="Dairy",
        description="1L low-fat milk"
    )
