# Importa o módulo 'db', que contém uma lista chamada 'vendas' com informações das vendas, e outros módulos necessários
from db import *
from utils import obter_ano_mes
from datetime import datetime

# Função para calcular os 3 melhores vendedores com base no ano e mês informados


def calcular_melhores_vendedores(ano, mes):
    # Cria um dicionário para armazenar as vendas de cada vendedor
    vendas_por_vendedor = {}

    # Percorre cada venda na lista 'vendas'
    for venda in vendas:
        # Converte a string da data de venda para um objeto datetime usando o formato especificado
        data_venda = datetime.strptime(venda["Data da Venda"], "%d/%m/%Y")

        # Verifica se a venda pertence ao ano e mês informados
        if data_venda.year == ano and data_venda.month == mes:
            # Obtém o nome do vendedor e o valor da venda
            nome_vendedor = venda["Nome do Vendedor"]
            valor_venda = venda["total_da_venda"]

            # Se o nome do vendedor já estiver no dicionário, adiciona o valor da venda ao total existente
            if nome_vendedor in vendas_por_vendedor:
                vendas_por_vendedor[nome_vendedor] += valor_venda
            else:
                # Caso contrário, cria uma nova entrada no dicionário com o nome do vendedor e o valor da venda
                vendas_por_vendedor[nome_vendedor] = valor_venda

    # Ordena o dicionário 'vendas_por_vendedor' com base nos valores (lucros) em ordem decrescente
    vendedores_ordenados = sorted(
        vendas_por_vendedor.items(), key=lambda x: x[1], reverse=True)

    # Cria uma lista com os três melhores vendedores e seus respectivos lucros (no máximo três se houver menos vendedores)
    melhores_vendedores = []
    for i in range(min(3, len(vendedores_ordenados))):
        vendedor, lucro = vendedores_ordenados[i]
        melhores_vendedores.append((vendedor, lucro))

    # Retorna a lista dos melhores vendedores
    return melhores_vendedores

# Função para exibir os três melhores vendedores do mês atual


def mostrar_melhores_vendedores():
    # Obtém o ano e mês atual usando a função 'obter_ano_mes' do módulo 'utils'
    ano, mes = obter_ano_mes()

    # Calcula os três melhores vendedores do mês atual usando a função 'calcular_melhores_vendedores'
    melhores_vendedores = calcular_melhores_vendedores(ano, mes)

    # Exibe o ranking dos melhores vendedores do mês atual
    print(f"\nRanking dos 3 melhores vendedores em {mes}/{ano}:\n")
    for vendedor, lucro in melhores_vendedores:
        print(f"{vendedor}: R${lucro:.2f}\n ")
