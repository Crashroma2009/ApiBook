from pydantic import BaseModel


class AuthorSchema(BaseModel):
    id: int
    name: str


class BookSchema(BaseModel):
    title: str
    genre: str
    author_id: int

    class Config:
        orm_mode = True
