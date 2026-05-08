from typing import List
from models import RegistroLavoura
import calculos, operacoes
import os

# Variáveis globais para controle do banco de dados e IDs
dados_fazenda: List[RegistroLavoura] = []
contador_id: int = 1

def limpar_tela() -> None:
    """Limpa o terminal de acordo com o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar() -> None:
    """Faz uma pausa para leitura antes de limpar a tela."""
    input("\nPressione Enter para continuar...")

def obter_entrada_valida() -> RegistroLavoura:
    """Coleta os dados, incluindo o nome do produto e cálculos de manejo."""

    print("--- Entrada de Dados de Manejo ---\n")
    print("[1] Soja | [2] Milho")
    
    tipo = int(input("Escolha a cultura: "))
    
    if tipo == 1:
        cultura = "Soja"
        area = calculos.calcular_area_soja(float(input("Base (m): ")), float(input("Altura (m): ")))
    
    elif tipo == 2:
        cultura = "Milho"
        area = calculos.calcular_area_milho(float(input("Base Maior (m): ")), float(input("Base Menor (m): ")), float(input("Altura (m): ")))
    
    else:
        raise ValueError("Cultura inválida.")

    produto = input("Nome do produto/insumo (ex: Fosfato, Fertilizante): ").strip()

    if not produto:
        raise ValueError("O nome do produto não pode ser vazio.")

    print(f"\nConfigurando aplicação de {produto}:")
    insumo_total = calculos.calcular_insumos(
        float(input(f"Dosagem de {produto} (mL/metro): ")),
        float(input("Comprimento da rua (m): ")),
        int(input("Quantidade de ruas: "))
    )

    return {
        "id": 0, 
        "cultura": cultura, 
        "produto": produto, 
        "area": area, 
        "insumo_total_litros": insumo_total
    }

def cadastrar() -> None:
    """Fluxo de cadastro com tratamento de erro."""

    limpar_tela()
    global contador_id

    try:
        novo = obter_entrada_valida()
        novo["id"] = contador_id
        operacoes.adicionar_registro(dados_fazenda, novo)
        contador_id += 1
        print("\n>>> Manejo registrado com sucesso!")

    except ValueError as e:
        print(f"\n[Erro] {e}")

    pausar()

def listar() -> None:
    """Exibe o relatório incluindo o produto utilizado."""

    limpar_tela()

    if not dados_fazenda:
        print("\n[!] Nenhum dado registrado.")

    else:
        print(f"{'ID':<4} | {'Cultura':<8} | {'Produto':<12} | {'Área(m²)':<10} | {'Total(L)':<8}")
        print("-" * 60)

        for r in dados_fazenda:
            print(f"{r['id']:<4} | {r['cultura']:<8} | {r['produto']:<12} | {r['area']:<10.2f} | {r['insumo_total_litros']:<8.2f}")

    pausar()

def atualizar() -> None:
    """Atualiza um registro existente."""
    
    listar()

    if not dados_fazenda: return

    try:
        id_alvo = int(input("\nID para atualizar: "))
        limpar_tela()
        novos_dados = obter_entrada_valida()
        novos_dados["id"] = id_alvo

        if operacoes.atualizar_registro(dados_fazenda, id_alvo, novos_dados):
            print("\n>>> Registro atualizado!")

        else:
            print("\n[Erro] ID não encontrado.")

    except ValueError as e:
        print(f"\n[Erro] {e}")

    pausar()

def deletar() -> None:
    """Remove um registro do vetor."""

    listar()

    if not dados_fazenda: return

    try:
        id_alvo = int(input("\nID para deletar: "))

        if operacoes.deletar_registro(dados_fazenda, id_alvo):
            print("\n>>> Registro removido.")

        else:
            print("\n[Erro] ID não encontrado.")

    except ValueError:
        print("\n[Erro] Entrada inválida.")

    pausar()

def main() -> None:
    """Função principal que controla o menu e o loop de execução do programa."""

    while True:
        print("\n--- FarmTech Solutions ---")
        print("1. Cadastrar | 2. Listar | 3. Atualizar | 4. Deletar | 5. Sair")
        opcao = input("Selecione: ")
        
        try:

            match opcao:
                case "1": cadastrar()
                case "2": listar()
                case "3": atualizar()
                case "4": deletar()
                case "5": break
                case _: print("Opção inválida.")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()