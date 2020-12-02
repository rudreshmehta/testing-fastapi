# -*- coding: utf-8 -*-
"""

@author: Rudresh
fastapi on ig media learn
"""

from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World1"}

@app.get("/welcome")
async def welcome(name:str):
    return {"welcome" : f'{name}'}

@app.get("/{nam}")
def welcome_name(nam:str):
    return {"name1":f'{nam}' + "tq"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

class Item(BaseModel):
    name: Optional[str] = "Rudresh1"
    price: float
    is_offer: bool = None
    print(name)


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[int] = None):
    return {"item_id": item_id, "q": q}
# ========================== None n set value function===================================================
# @app.get("/itemsqqq/{item_id}")
# def read_item(item_id: int, q: str = None):
#     if(q==None):
#         q="11111"
#     return {"item_id": item_id, "q": q}
# =============================================================================


@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)