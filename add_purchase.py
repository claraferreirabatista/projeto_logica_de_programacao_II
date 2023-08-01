# Importa os módulos necessários
from datetime import datetime
import random
from db import *  # Importa as classes de armazenamento de dados do arquivo db.py
from unidecode import unidecode

# Função que remove acentos e coloca em letras minúsculas
def trata_nome(nome):
    return unidecode(nome).lower() 

# Função para validar um CPF (apenas para fins ilustrativos)
def validar_cpf(cpf):
    # Remove pontos e traços do CPF, se houver
    cpf = cpf.replace('.', '').replace('-', '')
    # Verifica se o CPF tem 11 dígitos numéricos
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    return True  # Retorna True se o CPF for válido

# Função para validar uma data (apenas para fins ilustrativos)
def validar_data(data):
    try:
        # Extrai o dia, mês e ano da data informada
        dia, mes, ano = map(int, data.split('/'))
        # Verifica se a data está dentro de limites aceitáveis (2010 a 2023)
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 2010 <= ano <= 2023:
            return True
        else:
            return False
    except ValueError:
        return False

# Função para incluir uma nova venda
def inclui_venda():
    while True:
        # Gera um ID de venda aleatório
        venda_ID = random.randint(1008, 9999)
        # Solicita o nome do vendedor
        vendedor_nome = input("Digite o nome do vendedor: ")
        vendedor_encontrado = None
        # Procura o vendedor na lista de vendedores, ignorando acentos e letras maiúsculas
        for vendedor in vendedores:
            if trata_nome(vendedor.nome) == trata_nome(vendedor_nome):
                vendedor_encontrado = vendedor
                break
        if vendedor_encontrado is None:
            print("Vendedor não encontrado. Digite novamente.")
            continue

        # Solicita o CPF do comprador
        cpf_comprador = input("Digite o CPF do comprador: ")
        # Valida o CPF informado
        if not validar_cpf(cpf_comprador):
            print("CPF inválido. Digite novamente.")
            continue

        # Solicita a data da venda
        data_venda = input("Digite a data da venda (dd/mm/aaaa): ")
        # Valida a data informada
        if not validar_data(data_venda):
            print("Data inválida. Digite novamente.")
            continue

        # Cria uma nova instância da classe Venda com o ID e o vendedor encontrados
        nova_venda = Venda(venda_ID, vendedor_encontrado)

        while True:
            # Solicita o ID do produto
            produto_ID = int(input("Digite o ID do produto: "))
            produto_encontrado = None
            # Procura o produto na lista de produtos com base no ID informado
            for produto in produtos:
                if produto.id_produto == produto_ID:
                    produto_encontrado = produto
                    break
            if produto_encontrado is None:
                print("Produto não encontrado. Digite novamente.")
                continue

            # Solicita a quantidade do produto vendido
            quantidade = int(input("Digite a quantidade: "))

            # Adiciona o produto e a quantidade à nova venda
            nova_venda.adicionar_produto(produto_encontrado, quantidade)

            # Pergunta se deseja adicionar mais um produto à venda
            resposta = input("Deseja inserir mais um produto? (s/n): ").lower()
            if resposta not in {'s', 'sim'}:
                break

        # Adiciona a venda à lista de vendas
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
                # Cria uma lista de dicionários com informações dos produtos vendidos
                # usando a lista de produtos da instância de Venda criada
                for produto, quantidade in nova_venda.produtos.items()
            ],
            "total_da_venda": nova_venda.valor_total_da_venda
        })

        # Imprime informações sobre a venda realizada
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

        # Pergunta se deseja realizar outra venda
        resposta = input("Deseja realizar outra venda? (s/n): ").lower()
        if resposta not in {'s', 'sim'}:
            break
