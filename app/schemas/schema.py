from pydantic import BaseModel


class Author(BaseModel):
    id: int
    author: str | None

    class Config:
        orm_mode = True


class Book(BaseModel):
    id: int
    title: str
    price: int | float
    author_id: int

    class Config:
        orm_mode = True