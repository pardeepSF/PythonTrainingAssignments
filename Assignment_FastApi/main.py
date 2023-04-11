from fastapi import FastAPI
from typing import Optional

app =  FastAPI()

@app.get("/first")
def index():
    return "Fast Api Tutorial"

@app.get("/items/{item_id}")  #path parameter
def index(item_id: int):
    return {'product id':item_id}
