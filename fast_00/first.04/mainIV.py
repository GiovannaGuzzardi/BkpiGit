from fastapi import FastAPI
from typing import Optional

app = FastAPI()

books = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'}
}

# none: igual a nada se nada for passada


@app.get('/')
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = books.copy()
        del new_books[skip_book]
        return new_books
    return books


@app.get("/{book_name}")
async def read_book(book_name: str):
    return books[book_name]
