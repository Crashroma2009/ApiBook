from sqlalchemy.orm import relationship

from databases import engine

from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    book = relationship('Book')


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=True)
    author_id = Column(Integer, ForeignKey('author'))



