from typing import Union
from fastapi import APIRouter

root = APIRouter()

@root.get("/")
async def index():
    return {"status": "ok"}
