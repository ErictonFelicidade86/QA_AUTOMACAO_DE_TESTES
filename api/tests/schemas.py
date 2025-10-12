# tests/schemas.py
from pydantic import BaseModel, Field


class PostResponse(BaseModel):
    title: str
    body: str
    userId: int
    id: int = Field(gt=0)  # id inteiro > 0
