from sqlalchemy.orm import Session

from models import models
from schemas import schema


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_author(db: Session, author: schema.Author):
    db_author = models.Author(**author.dict(), book_id=author.id)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author




