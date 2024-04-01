from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import models


app = FastAPI()

class Volunteer(BaseModel):
    volunteer_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    date_of_birth: str
    address: str
    skills: str
    availability: dict[str, list]
    date_joined: str
    background_check: bool
    
items = []

@app.get("/api/volunteers", response_model=List[Volunteer])
async def read_items():
    return items

@app.post("/api/volunteers", response_model=Volunteer)
async def create_item(item: Volunteer):
    items.append(item)
    return item

@app.put("/api/volunteers/{volunteerId}", response_model=Volunteer)
async def update_item(item_id: int, item: Volunteer):
    items[item_id] = item
    return item

@app.delete("/api/volunteers/{volunteerId}")
async def delete_item(item_id: int):
    del items[item_id]
    return {"message": "Item deleted"}


models.Base.metadata.create_all(bind= engine)
