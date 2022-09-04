from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey

from databases import Base


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    books = relationship('Book', backref='book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship('Author', backref='author')






