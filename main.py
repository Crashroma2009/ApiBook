from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import schemas
from models import Author, Book
from databases import Base, engine
from dependency import get_db


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/authors/", response_model=list[schemas.Author])
def read_author_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    #authors = crud.get_authors_all(db)
    if not authors:
        raise HTTPException('Not authors')
    return authors


@app.get('/books/', response_model=list[schemas.Book])
def read_books_all(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    if not books:
        raise HTTPException('Not books')
    return books










