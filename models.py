"""
model class
"""
from sqlalchemy import create_engine, Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    """Author model
    """
    __tablename__ = 'books_author'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    birth_year = Column(SmallInteger)
    death_year = Column(SmallInteger)

class Language(Base):
    """Language model
    """
    __tablename__ = 'books_language'
    
    id = Column(Integer, primary_key=True)
    code = Column(String(4), nullable=False)

class Bookshelf(Base):
    """Bookshelf model
    """
    __tablename__ = 'books_bookshelf'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)

class Subject(Base):
    """Subject model
    """
    __tablename__ = 'books_subject'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

class Book(Base):
    """Book model
    """
    __tablename__ = 'books_book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    download_count = Column(Integer, default=0)

    authors = relationship("Author", secondary="books_book_authors")
    languages = relationship("Language", secondary="books_book_languages")
    subjects = relationship("Subject", secondary="books_book_subjects")
    bookshelves = relationship("Bookshelf", secondary="books_book_bookshelves")
    formats = relationship("BookFormat", back_populates="book")

# Many-to-many relationship tables
class BookAuthors(Base):
    """Book Author model
    """
    __tablename__ = 'books_book_authors'
    
    book_id = Column(Integer, ForeignKey('books_book.id'), primary_key=True)
    author_id = Column(Integer, ForeignKey('books_author.id'), primary_key=True)

class BookLanguages(Base):
    """Book lanugauge model
    """
    __tablename__ = 'books_book_languages'
    
    book_id = Column(Integer, ForeignKey('books_book.id'), primary_key=True)
    language_id = Column(Integer, ForeignKey('books_language.id'), primary_key=True)

class BookSubjects(Base):
    """Book subject model
    """
    __tablename__ = 'books_book_subjects'
    
    book_id = Column(Integer, ForeignKey('books_book.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('books_subject.id'), primary_key=True)

class BookBookshelves(Base):
    """Book bookshelves model
    """
    __tablename__ = 'books_book_bookshelves'
    
    book_id = Column(Integer, ForeignKey('books_book.id'), primary_key=True)
    bookshelf_id = Column(Integer, ForeignKey('books_bookshelf.id'), primary_key=True)

class BookFormat(Base):
    """Book format model
    """
    __tablename__ = 'books_format'
    
    id = Column(Integer, primary_key=True)
    mime_type = Column(String(32), nullable=False)
    url = Column(String(256), nullable=False)
    book_id = Column(Integer, ForeignKey('books_book.id'))
    book = relationship("Book", back_populates="formats")

