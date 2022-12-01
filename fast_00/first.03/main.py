from enum import Enum

from fastapi import FastAPI

app = FastAPI()

books = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'}
}

# read the book(get) , create new book(post), update a book(put or patch),
# delete a book(delete)
# crud operations
# rest APIs : http request methods

# GET/ get all the books
# GET / book_1 get book1 -> object(title and the author)

# put/book_2 -> update book2

# post/ create new book

# DELETE/book_3 delete book3

# enum , um Enum recebe um str. Classe só tem essas 5 opções


class DirectionName(str, Enum):  # class
    north = "North"
    south = "South"
    east = "East"
    west = "West"


@app.get('/')
async def read_all_books():
    return books


@app.get('/direction/{direction_nome}')
# tipagem de direction_nome é DirectionNOme
# retorna um dicionario com dois itens
# um dos itens é definido por receimentos de argumentos
async def get_direction(direction_nome: DirectionName):
    if direction_nome == DirectionName.north:
        return {"Direction:": direction_nome, "sub": "up"}
    if direction_nome == DirectionName.south:
        return {"Direction:": direction_nome, "sub": "down"}
    if direction_nome == DirectionName.east:
        return {"Direction:": direction_nome, "sub": "left"}
    return {"Direction:": direction_nome, "sub": "right"}


@app.get("/books/mybook")
async def read_favorite_books():
    return {"book_title": "my favorite book"}


@app.get("")
@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_title": book_id}
