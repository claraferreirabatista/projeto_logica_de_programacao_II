from db import *

# Função para excluir uma venda com base em seu 'id_venda'.
def excluir_venda_por_id(id_venda):
    # Percorre a lista de vendas usando a função enumerate para obter o índice (i) e o valor (venda) atual.
    for i, venda in enumerate(vendas):
        # Verifica se o 'id_venda' da venda atual coincide com o 'id_venda' que queremos excluir.
        if venda['id_venda'] == id_venda:
            # Se encontrarmos uma venda com o 'id_venda' desejado, a excluímos usando 'del'.
            del vendas[i]
            # Retornamos True para indicar que a venda foi excluída com sucesso.
            return True
    # Se não encontrarmos nenhuma venda com o 'id_venda' fornecido, retornamos False.
    return False

# Função para permitir a exclusão de uma venda com base no 'id_venda' informado pelo usuário.
def exclui_venda():
    # Iniciamos um loop infinito para que o usuário possa excluir várias vendas, se desejar.
    while True:
        # Solicita ao usuário que digite o 'id_venda' da venda que ele deseja excluir.
        id_venda_excluir = int(input("Digite o ID da venda que deseja excluir: "))
        # Chamamos a função 'excluir_venda_por_id' passando o 'id_venda' informado pelo usuário.
        # Se a função retornar True, significa que a venda foi excluída com sucesso.
        if excluir_venda_por_id(id_venda_excluir):
            print(f"\n Venda com ID {id_venda_excluir} excluída com sucesso.")
        else:
            # Caso contrário, a venda não foi encontrada na lista 'vendas'.
            print(f"Venda com ID {id_venda_excluir} não encontrada.")

        # Pergunta ao usuário se ele deseja excluir mais uma venda.
        resposta = input("Deseja excluir mais uma venda? (s/n): ").lower()
        # Se a resposta não for 's' ou 'sim', significa que o usuário não quer excluir mais vendas.
        # Então, saímos do loop infinito com 'break'.
        if resposta not in {'s', 'sim'}:
            break