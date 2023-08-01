# Importando o módulo 'db', que deve conter funcionalidades relacionadas ao banco de dados.
# Presume-se que nesse módulo há uma estrutura de dados 'dados' e funcionalidades para manipulá-la.
from db import *

# Função para salvar os dados em um arquivo especificado pelo 'nome_arquivo'.
# Ela recebe 'dados' como entrada e os salva no arquivo usando a função 'write()' do arquivo aberto.
def salvar_dados_em_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(str(dados))

# Função para converter os valores de vendas e produtos para dólar, com base em uma taxa de conversão.
# Ela itera sobre cada venda em 'dados', faz cópia da venda original e ajusta os valores para dólar.
# Para cada produto na venda, também converte o valor do produto para dólar.
def converter_valores_para_dolar(dados, taxa=0.2):
    for venda in dados:
        venda_convertida = venda.copy()
        venda_convertida['total_da_venda'] = venda['total_da_venda'] * taxa
        venda_convertida['Produtos'] = [
            {
                "produto_id": produto['produto_id'],
                "nome_do_produto": produto['nome_do_produto'],
                "valor_do_produto": produto['valor_do_produto'] * taxa,
                "quantidade": produto['quantidade']
            }
            for produto in venda['Produtos']
        ]
        # A função usa 'yield' para retornar um gerador, em vez de uma lista, economizando memória.
        yield venda_convertida

# Função para salvar os valores convertidos para dólar em um arquivo especificado pelo 'nome_arquivo'.
# Ela chama a função 'converter_valores_para_dolar' para obter as vendas convertidas e, em seguida,
# salva essa lista de vendas no arquivo usando a função 'write()' do arquivo aberto.
def salvar_valores_em_dolar_em_arquivo(dados, nome_arquivo, taxa=0.2):
    # Obtém a lista de vendas convertidas para dólar
    vendas_convertidas = list(converter_valores_para_dolar(dados, taxa))
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(str(vendas_convertidas))
