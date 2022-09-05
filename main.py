from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models, schemas
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


@app.post('/author/', response_model=schemas.Author)
def create_author(author: schemas.Author, db: Session = Depends(get_db)):
    add_author = models.Author(name=author.name)
    db.add(add_author)
    db.commit()
    db.refresh(add_author)
    return add_author


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


@app.post('/book/', response_model=schemas.Book)
def create_book(book: schemas.Book, db: Session = Depends(get_db)):
    add_book = models.Book(title=book.title, genre=book.genre, author_id=book.author_id)
    db.add(add_book)
    db.commit()
    db.refresh(add_book)
    return add_book




