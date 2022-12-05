from typing import Optional  # deixa uma ação opcional
from uuid import UUID  # id chave primaria

from fastapi import FastAPI
# validação de dados , field validação extra
from pydantic import BaseModel, Field

app = FastAPI()

BOOKS = list()


def criar_livroFun():
    book_1 = Book(id="a48cbd47-5823-4b7b-b13e-db08f0daea3a",
                  titulo="title 1",
                  autor="autor 1",
                  descrição="sla cara",
                  nota=60)
    book_2 = Book(id="b48cbd47-5823-4b7b-b13e-db08f0daea3a",
                  titulo="title 2",
                  autor="autor 2",
                  descrição="sla cara",
                  nota=70)
    book_3 = Book(id="c48cbd47-5823-4b7b-b13e-db08f0daea3a",
                  titulo="title 3",
                  autor="autor 3",
                  descrição="sla cara",
                  nota=80)
    book_4 = Book(id="d48cbd47-5823-4b7b-b13e-db08f0daea3a",
                  titulo="title 4",
                  autor="autor 4",
                  descrição="sla cara",
                  nota=100)
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)

# get/<book uuid > livro especifico
# put/<book uuid> atualizar livro
# post criar novo livro
# delete deletar livro especifico

# fiz ele entender BaseModel e ter validação automatica
# objeto dentro do python


class Book(BaseModel):
    id: UUID
    # agora só fica valido se tiver ao menos 1 caracter
    titulo: str = Field(min_length=1, max_length=50)
    autor: str = Field(min_length=1, max_length=50)
    descrição: Optional[str] = Field(title="descrição desse livro",
                                     max_length=100, min_length=1)
    # title: descreve o que deve ser inserido
    # max : maximo de letras
    # min: minimo de letras
    # optional : pode ser nula
    nota: int = Field(gt=-1, lt=101)  # maior que -1 e menor que 101


# get/ consulta todos os livros
@app.get('/')
async def consulta():
    if len(BOOKS) < 1:
        criar_livroFun()
    return BOOKS

# post criar novo livro


@app.post('/')
async def criar_livro(book: Book):
    BOOKS.append(book)
    return book
