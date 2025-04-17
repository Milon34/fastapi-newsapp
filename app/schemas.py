from pydantic import BaseModel
from datetime import datetime


class NewsBase(BaseModel):
    title: str
    description: str = None
    url: str
    publishedAt: datetime


class NewsCreate(NewsBase):
    pass


class NewsOut(NewsBase):
    id: int

    class Config:
        orm_mode = True
