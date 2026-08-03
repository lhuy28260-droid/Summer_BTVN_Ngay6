from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class BookCreate(BaseModel):
    title: str
    author: str
    price: float
    pages: int

class BookResponse(BookCreate):
    id: int


# BÀI 2: API ENDPOINTS & DATABASE GIẢ LẬP 
books_db = []
book_id_counter = 1


# 2. Endpoint POST /books: Thêm sách mới
@app.post("/books", response_model=BookResponse)
def create_book(book: BookCreate):
    global book_id_counter
    
    new_book = book.model_dump()
    new_book["id"] = book_id_counter
    
    
    books_db.append(new_book)
    
    book_id_counter += 1
    
    return new_book


@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
            
    raise HTTPException(status_code=404, detail="Book not found")