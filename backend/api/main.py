import asyncio
from fastapi import FastAPI
from services.service import get_news
from routers import router
from cruds.news import db_create_news

app = FastAPI()
app.include_router(router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

async def update_news_periodically():
    # get_news()
    data = {
    "Name":"test3",
    "Age":25,
}
    db_create_news(data)
    pass

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(update_news_periodically())