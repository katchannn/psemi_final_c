import asyncio
from fastapi import FastAPI
from routers import news
from cruds import news as news_crud

app = FastAPI()
app.include_router(news.router)

async def update_news_periodically():
    # while True:
    #     await update_news()  # update_news関数を実行
    #     await asyncio.sleep(3600)  # 1時間ごとに更新 

    
    news_crud.db_get_news(0)#get_newsの確認のため
    
    
    

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(update_news_periodically())