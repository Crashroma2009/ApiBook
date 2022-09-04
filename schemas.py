from pydantic import BaseModel

from models import Author, Book


class AuthorSchema(BaseModel):
    name: str


class AuthorCreate(AuthorSchema):
    pass


class Author(AuthorSchema):
    id: int

    class Config:
        orm_mode = True


# class AuthorBookSchema(AuthorSchema):
#     books: Book


class BookSchema(BaseModel):
    title: str
    genre: str


class BookCreate(Book):
    pass


class Book(BookSchema):
    id: int
    author_id: int

    class Config:
        orm_mode = True
