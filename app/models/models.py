from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    price = Column(Integer, default=None)
    author_id = Column(Integer, ForeignKey('author.id'))

