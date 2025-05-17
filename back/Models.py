# models.py
from pydantic import BaseModel
from typing import Optional, List

class PokemonModel(BaseModel):
    id: str
    active: bool
    name: str
    height: Optional[int] = None
    weight: Optional[int] = None
    types: Optional[List[str]] = []
    sprites: str
