from datetime import datetime
import random
from db import *

def validar_cpf(cpf):
# Implementação básica de validação do CPF (apenas para fins ilustrativos)
# Remover pontos e traços, se houver
    cpf = cpf.replace('.', '').replace('-', '')
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    return True  # Retornar True se o CPF for válido

def validar_data(data):
# Implementação básica de validação da data (apenas para fins ilustrativos)
    try:
        dia, mes, ano = map(int, data.split('/'))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 2010 <= ano <= 2023:
            return True
        else:
            return False
    except ValueError:
        return False

def inclui_venda():

    while True:
        venda_ID = random.randint(1008, 9999)
        vendedor_nome = input("Digite o nome do vendedor: ")
        vendedor_encontrado = None
        for vendedor in vendedores:
            if vendedor.nome.lower() == vendedor_nome.lower():
                vendedor_encontrado = vendedor
                break
        if vendedor_encontrado is None:
            print("Vendedor não encontrado. Digite novamente.")
            continue

        cpf_comprador = input("Digite o CPF do comprador: ")
        if not validar_cpf(cpf_comprador):
            print("CPF inválido. Digite novamente.")
            continue

        data_venda = input("Digite a data da venda (dd/mm/aaaa): ")
        if not validar_data(data_venda):
            print("Data inválida. Digite novamente.")
            continue

        nova_venda = Venda(venda_ID, vendedor_encontrado)

        while True:
            produto_ID = int(input("Digite o ID do produto: "))
            produto_encontrado = None
            for produto in produtos:
                if produto.id_produto == produto_ID:
                    produto_encontrado = produto
                    break
            if produto_encontrado is None:
                print("Produto não encontrado. Digite novamente.")
                continue

            quantidade = int(input("Digite a quantidade: "))

            nova_venda.adicionar_produto(produto_encontrado, quantidade)

            resposta = input("Deseja inserir mais um produto? (s/n): ").lower()
            if resposta not in {'s', 'sim'}:
                break

        vendas.append({
            "id_venda": nova_venda.venda_ID,
            "Nome do Vendedor": nova_venda.vendedor.nome,
            "CPF do Comprador": cpf_comprador,
            "Data da Venda": data_venda,
            "Produtos": [
                {
                    "produto_id": produto.id_produto,
                    "nome_do_produto": produto.nome,
                    "valor_do_produto": produto.valor
                }
                # Correção do método items() no lugar de values()
                for produto, quantidade in nova_venda.produtos.items()
            ],
            "total_da_venda": nova_venda.valor_total_da_venda
        })

        print(f"\n Venda ID: {vendas[-1]['id_venda']}")
        print(f"Nome do Vendedor: {vendas[-1]['Nome do Vendedor']}")
        print(f"CPF do Comprador: {vendas[-1]['CPF do Comprador']}")
        print(f"Data da Venda: {vendas[-1]['Data da Venda']}")
        print("Produtos:")
        for produto in vendas[-1]['Produtos']:
            print(f"- Produto ID: {produto['produto_id']}")
            print(f"  Nome do Produto: {produto['nome_do_produto']}")
            print(f"  Valor do Produto: R$ {produto['valor_do_produto']:.2f}")
        print(f"Total da Venda: R$ {vendas[-1]['total_da_venda']:.2f}\n")

        resposta = input("Deseja realizar outra venda? (s/n): ").lower()
        if resposta not in {'s', 'sim'}:
            break
