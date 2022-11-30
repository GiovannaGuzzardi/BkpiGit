from typing import Optional

from pydantic import BaseModel


class Curso(BaseModel):  # validaçao de dados
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
