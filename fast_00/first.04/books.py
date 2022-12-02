from typing import Optional

from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'}
}

# none: igual a nada se nada for passado
# recebe uma variavel (skip_book) opcional e retorna dicionario de livros


@app.get('/')
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0
    if len(BOOKS) > 0:  # se tamanho maior que 0
        for book in BOOKS:  # passa por todas as key
            x = int(book.split('_')[-1])  # split separa book por _ do digito
            if x > current_book_id:
                current_book_id = x  # faz com que o id seja do ultimo
    BOOKS[f'book_{current_book_id+1}'] = {'title': book_title,
                                          'author': book_author}  # adiciona id e itens no id
    return BOOKS[f'book_{current_book_id+1}']  # retorna id criado
