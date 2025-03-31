from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import hashlib
import asyncio

app = FastAPI()
url_storage = {}

class UrlData(BaseModel):
    url: str

def generate_short_id(url: str) -> str:
    return hashlib.sha256(url.encode()).hexdigest()[:6]

@app.post("/")
async def shorten_url(data: UrlData):
    short_id = generate_short_id(data.url)
    url_storage[short_id] = data.url
    return {"short_id": short_id}

@app.get("/async-data")
async def async_data():
    await asyncio.sleep(2)
    return {"status": "done"}

@app.get("/{short_id}")
async def redirect(short_id: str):
    if short_id not in url_storage:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url_storage[short_id], status_code=307)