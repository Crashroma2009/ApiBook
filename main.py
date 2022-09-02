from fastapi import FastAPI, HTTPException
from models.databases import Base
from sqlalchemy.orm import sessionmaker
from models.models import Author, Book
from models.databases import session
from models.schemas import BookSchema


app = FastAPI()
#
# engine = engine
# DBSession = sessionmaker(bind=engine)
# Base.metadata.bind = engine
#
# session = DBSession()


@app.get('books/', response_model=BookSchema)
def index():
    books = db.query(Book).all()
    if not books:
        raise HTTPException
    return {'data': 'Hello world'}


@app.get('/authors')
def author_all():
    return session.query(Author.name).all()







