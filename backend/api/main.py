import asyncio
from fastapi import FastAPI
from services.news import get_news
from routers import news
from cruds import news as news_crud
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(news.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def update_news_periodically():
    print("起動")#デバッグプリント
    while True:
        print("get_newsを開始")
        await get_news()  # get_news関数を実行



@app.on_event("startup")
async def on_startup():
    print("初回起動")#デバッグプリント
    asyncio.create_task(update_news_periodically())
