from fastapi import APIRouter

router = APIRouter()

@router.get("/news")
async def newsList():
    pass

@router.get("/news/{news_id}")
async def newsDetail():
    pass