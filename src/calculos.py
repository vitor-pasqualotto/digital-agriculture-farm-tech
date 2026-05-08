import math

def validar_positivo(valor: float, nome_campo: str) -> None:
    """Garante que medidas físicas não sejam negativas ou zero."""
    if valor <= 0:
        raise ValueError(f"O campo '{nome_campo}' deve ser maior que zero")

def calcular_area_soja(base, altura: float) -> float:
    """Calcula área retangular para soja"""

    validar_positivo(base, 'Base')
    validar_positivo(altura, 'Altura')

    return base * altura

def calcular_area_milho(base_maior, base_menor, altura: float) -> float:
    """Calcula a área para cultura de Milho."""

    validar_positivo(base_maior, 'Base')
    validar_positivo(base_menor, 'Base')
    validar_positivo(altura, 'Altura')

    return ((base_maior + base_menor) * altura) / 2

def calcular_insumos(qntd_ml_por_metro, comprimento_rua: float, num_ruas: int) -> float:
    """
    Calcula o total de insumos necessários.
    Retorna o valor convertido para Litros (L).
    """
    
    validar_positivo(qntd_ml_por_metro, 'ML por metro')
    validar_positivo(comprimento_rua, 'Comprimento da rua')
    validar_positivo(num_ruas, 'Número de ruas')

    total_ml: float = qntd_ml_por_metro * comprimento_rua * num_ruas
    return total_ml / 1000