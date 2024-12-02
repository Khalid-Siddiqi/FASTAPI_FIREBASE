from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price: float
    is_offer:bool = None
    tax:float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/")
async def root():
    return{"message": "Hello World"}

@app.get("/items/{items_id}")
async def read_item(items_id:int):
    return{"item_id": items_id}
#http://127.0.0.1:8000/items/4
#{"item_id":4}
@app.get("/items/")
async def read_item(item_id: int, q: str=None):
    return{"item_id": item_id, "q": q}
# http://127.0.0.1:8000/items/?item_id=12&q=khalid
# {"item_id":12,"q":"khalid"}

