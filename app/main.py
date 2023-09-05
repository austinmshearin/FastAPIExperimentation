# Standard Imports
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Get request with no parameters
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get request with parameter from url
@app.get("/{id}")
async def get_id(id: int):
    return id

# Get request with optional parameters
@app.get("/get/")
async def get_stuff(x: int | None = None, y: int | None = None):
    return {"x": x, "y": y}

# Post request with JSON data matching the base model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return item
