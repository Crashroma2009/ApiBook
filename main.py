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
        raise HTTPException(status_code=404,  detail='Not authors')
    return authors


@app.get('/author/{author_id}', response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).get(author_id)
    if not author:
        raise HTTPException(status_code=404, detail='Not id author')
    return author


@app.get('/books/', response_model=list[schemas.Book])
def read_books_all(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail='Not books')
    return books


@app.get('/book/{book_id}', response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail='Not id book')
    return book








