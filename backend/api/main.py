import asyncio
from fastapi import FastAPI
from services.service import get_news

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


async def update_news_periodically():
    get_news()

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(update_news_periodically())