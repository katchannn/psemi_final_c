from pydantic import BaseModel


class News(BaseModel):
    id: str
    html: str
    img: str
    title: str
    keywords: dict
    content: str
