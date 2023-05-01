from fastapi import APIRouter

router = APIRouter()

@router.get("/news")
async def list_news():
    pass

@router.get("/news/{news_id}")
async def detail_news():
    pass

@router.get("/news/test")
async def test_news():
    pass