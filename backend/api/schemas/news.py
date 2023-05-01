from typing import Optional
from pydantic import BaseModel, Field


class News(BaseModel):
    id: int
    title: str
    keywords: dict
    content: str
