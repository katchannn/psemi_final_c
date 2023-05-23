from pydantic import BaseModel


class News(BaseModel):
    id: str #変更 idの16進数をどう表すか問題
    htmlsrc: str
    imgsrc: str
    title: str
    keywords: dict
    content: str
