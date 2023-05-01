import asyncio
from fastapi import FastAPI
from routers import news

app = FastAPI()
app.include_router(news.router)

async def update_news_periodically():
    pass

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(update_news_periodically())