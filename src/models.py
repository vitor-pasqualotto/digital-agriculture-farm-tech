from typing import TypedDict

class RegistroLavoura(TypedDict):
    id: int
    cultura: str
    produto: str
    area: float
    insumo_total_litros: float