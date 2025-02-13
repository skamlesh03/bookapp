"""
main api script
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from schema import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from models import Base, Author, Language, Bookshelf, Subject, Book, BookAuthors, BookLanguages, BookSubjects, BookBookshelves, BookFormat
from database import get_db
from schema import BookResponse

# FastAPI app initialization
app = FastAPI()

@app.get("/books", response_model=List[BookResponse])
def get_books(
    title: Optional[str] = None,
    author: Optional[str] = None,
    language: Optional[str] = None,
    topic: Optional[str] = None,
    page: int = 1,
    db: Session = Depends(get_db)
):
    """
    Endpoint to retrieve books based on filters
    """
    # Apply filters
    query = db.query(Book).join(BookAuthors).join(Author).join(BookLanguages).join(Language)
    
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Author.name.ilike(f"%{author}%"))
    if language:
        lang_list = language.split(',')
        if len(lang_list) > 1:
            print("=============================")
            query = handle_muliple_value(lang_list, Language, query)
        else:
            query = query.filter(Language.code.ilike(f"%{language}%"))
    if topic:
        query = query.filter(Subject.name.ilike(f"%{topic}%") | Bookshelf.name.ilike(f"%{topic}%"))
    
    # Paginate and order by download_count => descending
    books = query.order_by(Book.download_count.desc()).offset((page - 1) * 25).limit(25).all()

    # Create response data
    result = []
    for book in books:
        result.append(BookResponse(
            title=book.title,
            author=", ".join([a.name for a in book.authors]),
            genre="Fiction",  # Can be derived from subjects or genres
            language=", ".join([l.code for l in book.languages]),
            subjects=[s.name for s in book.subjects],
            bookshelves=[b.name for b in book.bookshelves],
            download_links=[f.url for f in book.formats]
        ))
    
    return result

def handle_muliple_value(input_list, tableName, query):
    for data in input_list:
        query = query.filter(tableName.code.ilike(f"%{data}%"))
    return query