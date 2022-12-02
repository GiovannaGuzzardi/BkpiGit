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

# pega um item ja existente ou coleção


@app.get('/')
async def read_all_books(skip_book: Optional[str] = None):
    # none: igual a nada se nada for passado
    # recebe uma variavel (skip_book) opcional e retorna dicionario de livros
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS
# http://127.0.0.1:8000/?skip_book=book_2
# o opcional se torna uma query
# se não for usada não aparece


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]

# adiciona um item na coleção


@app.post("/")
async def create_book(book_title, book_author):
    # recebe dois argumentos que alteram o recurso
    current_book_id = 0
    if len(BOOKS) > 0:  # se tamanho maior que 0
        for book in BOOKS:  # passa por todas as key
            x = int(book.split('_')[-1])  # split separa book por _ do digito
            if x > current_book_id:
                current_book_id = x  # faz com que o id seja do ultimo
    BOOKS[f'book_{current_book_id+1}'] = {'title': book_title,
                                          'author': book_author}
    # adiciona id e itens no id
    return BOOKS[f'book_{current_book_id+1}']  # retorna id criado
    # como não tem um banco de dados assim que fechamos o servidor
    # o item é perdido

# modifica um item da coleção


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    # recebe name como localizador e os outros dois itens para alteração
    book_information = {'title': book_title, 'author': book_author}
    # cria um segundo dicionario para fazer a devolução
    BOOKS[book_name] = book_information
    return book_information


@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted'
# http: // 127.0.0.1: 8000/book_4


@app.get('/assigment/')
async def read_book_exerc(book_name: str):
    return BOOKS[book_name]


@app.delete('/assigment/')
async def delete_book_exerc(book_name: str):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted'
# http://127.0.0.1:8000/assigment/?book_name=book_2
