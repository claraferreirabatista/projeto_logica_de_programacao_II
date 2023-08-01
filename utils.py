# Importa as classes Vendedor e Produto do módulo db
from db import *

# Importa as classes datetime e timedelta do módulo datetime
from datetime import datetime, timedelta

# Importa o módulo calendar para obter informações sobre o calendário
import calendar

def obter_ano_mes():
    while True:
        try:
            # Solicita ao usuário que digite o ano e o converte para um valor inteiro
            ano = int(input("Digite o ano (entre 2010 e 2023): "))

            if 2010 <= ano <= 2023:
                # Se o ano for válido, sai do loop infinito
                break
            else:
                # Caso contrário, imprime uma mensagem de erro e o loop continua
                print("Ano inválido! O ano deve estar entre 2010 e 2023.")
        except ValueError:
            # Caso ocorra uma exceção ao converter o ano para inteiro, imprime uma mensagem de erro e o loop continua
            print("Ano inválido! Digite um número válido para o ano.")

    while True:
        try:
            # Solicita ao usuário que digite o mês e o converte para um valor inteiro
            mes = int(input("Digite o mês : "))
            # Verifica se o mês está dentro do intervalo válido (1 a 12)
            if 1 <= mes <= 12:
                # Se o mês for válido, sai do loop infinito
                break
            else:
                # Caso contrário, imprime uma mensagem de erro e o loop continua
                print("Mês inválido! O mês deve estar no intervalo de 1 a 12.")
        except ValueError:
            # Caso ocorra uma exceção ao converter o mês para inteiro, imprime uma mensagem de erro e o loop continua
            print("Mês inválido! Digite um número válido para o mês.")

    # Retorna o ano e o mês digitados pelo usuário
    return ano, mes

# Define a função para criar um dicionário com produtos mapeados por ID
def criar_dicionario_produtos_por_id(produtos):
    # Cria um dicionário vazio para armazenar os produtos mapeados por ID
    produtos_por_id = {}
    # Percorre a lista de produtos recebida como parâmetro
    for produto in produtos:
        # Mapeia o ID do produto para o nome do produto no dicionário
        produtos_por_id[produto.id_produto] = produto.nome
    # Retorna o dicionário com os produtos mapeados por ID
    return produtos_por_id

# Define a função para calcular as vendas totais e produtos vendidos em um determinado mês e ano
def calcular_vendas_por_mes_ano(vendas, ano_referencia, mes_referencia):
    # Inicializa as variáveis para armazenar as vendas totais e os produtos vendidos
    total_vendas_mes_ano = 0
    produtos_vendidos = {}

    # Percorre cada venda da lista de vendas
    for venda in vendas:
        # Converte a data da venda para o formato de objeto datetime
        data_venda = datetime.strptime(venda["Data da Venda"], "%d/%m/%Y")
        # Verifica se a venda ocorreu no ano e mês de referência
        if data_venda.year == ano_referencia and data_venda.month == mes_referencia:
            # Se sim, adiciona o valor total da venda ao total de vendas do mês e ano de referência
            total_vendas_mes_ano += venda["total_da_venda"]
            # Percorre cada produto vendido na venda
            for produto in venda["Produtos"]:
                # Obtém o ID do produto e a quantidade vendida
                produto_id = produto["produto_id"]
                quantidade_vendida = produto["quantidade"]
                # Atualiza o dicionário de produtos vendidos com o ID do produto e a quantidade vendida
                if produto_id in produtos_vendidos:
                    produtos_vendidos[produto_id] += quantidade_vendida
                else:
                    produtos_vendidos[produto_id] = quantidade_vendida

    # Retorna o total de vendas do mês e ano de referência e o dicionário de produtos vendidos
    return total_vendas_mes_ano, produtos_vendidos