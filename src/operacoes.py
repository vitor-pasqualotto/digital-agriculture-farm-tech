from typing import List
from models import RegistroLavoura

def adicionar_registro(vetor: List[RegistroLavoura], registro: RegistroLavoura) -> None:
    """Adiciona um novo registro de lavoura ao vetor de dados."""
    vetor.append(registro)

def deletar_registro(vetor: List[RegistroLavoura], id_alvo: int) -> bool:
    """Busca e remove um registro do vetor através do ID informado."""

    for i, reg in enumerate(vetor):
        if reg['id'] == id_alvo:
            vetor.pop(i)
            return True
    return False

def atualizar_registro(vetor: List[RegistroLavoura], id_alvo: int, novos_dados: RegistroLavoura) -> bool:
    """Substitui os dados de um registro existente no vetor com base no ID."""

    for i, reg in enumerate(vetor):
        if reg['id'] == id_alvo:
            vetor[i] = novos_dados
            return True
    return False
