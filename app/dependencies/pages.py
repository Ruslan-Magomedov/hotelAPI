from fastapi import Depends, Query
from pydantic import BaseModel

from typing import Annotated


class Pagenation(BaseModel):
    """Проверка и ограничение данных"""
    page: Annotated[int, Query(default=1, ge=1)]
    quantity: Annotated[int, Query(default= 3, ge=3, le=10)]


PagenationDep = Annotated[Pagenation, Depends()]
