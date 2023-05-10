from pydantic import BaseModel


class News(BaseModel):
    id: int
    title: str
    keywords: dict
    content: str
