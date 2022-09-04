from pydantic import BaseModel

from models import Book


class AuthorSchema(BaseModel):
    name: str


class AuthorCreate(AuthorSchema):
    pass


class Author(AuthorSchema):
    id: int
    name: str
    #books: list[Book] = []

    class Config:
        orm_mode = True


class BookSchema(BaseModel):
    title: str
    genre: str


class BookCrate(BookSchema):
    pass


class Book(BookSchema):
    id: int
    author_id: int

    class Config:
        orm_mode = True
