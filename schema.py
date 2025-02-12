from pydantic import BaseModel
from typing import List

class BookResponse(BaseModel):
    title: str
    author: str
    genre: str
    language: str
    subjects: List[str]
    bookshelves: List[str]
    download_links: List[str]
    
    class Config:
        orm_mode = True