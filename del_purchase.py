from db import *

def excluir_venda_por_id(id_venda):
    for i, venda in enumerate(vendas):
        if venda['id_venda'] == id_venda:
            del vendas[i]
            return True
    return False

def exclui_venda():
    while True:

        id_venda_excluir = int(input("Digite o ID da venda que deseja excluir: "))
        if excluir_venda_por_id(id_venda_excluir):
            print(f"Venda com ID {id_venda_excluir} excluída com sucesso.")
        else:
            print(f"Venda com ID {id_venda_excluir} não encontrada.")

        resposta = input("Deseja excluir mais uma venda? (s/n): ").lower()
        if resposta not in {'s', 'sim'}:
            break