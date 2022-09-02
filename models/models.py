from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey

from databases import Base, engine


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship('Author')


if __name__ == '__main__':
    Base.metadata.create_all(engine)



