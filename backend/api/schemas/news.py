from typing import Optional
from pydantic import BaseModel, Field


class Keyword(BaseModel):
    keyword: str = Field(None, example="keyword")
    keyword_description: str = Field(None, example="keyword_description")


class News(BaseModel):
    id: int
    title: str = Field(None, example="title")
    keywords: list[Keyword] = Field(
        None,
        example=[
            {"keyword": "keyword1", "keyword_description": "keyword_description1"},
            {"keyword": "keyword2", "keyword_description": "keyword_description2"},
            {"keyword": "keyword3", "keyword_description": "keyword_description3"},
        ],
    )
    content: str = Field(None, example="content")
