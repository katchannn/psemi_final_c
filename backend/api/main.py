import asyncio
from fastapi import FastAPI
from services.news import get_news
from routers import news
from cruds import news as news_crud

app = FastAPI()
app.include_router(news.router)

async def update_news_periodically():
    print("起動")#デバッグプリント
    while True:
        print("get_newsを開始")
        await get_news()  # get_news関数を実行


@app.on_event("startup")
async def on_startup():
    print("初回起動")#デバッグプリント
    asyncio.create_task(update_news_periodically())