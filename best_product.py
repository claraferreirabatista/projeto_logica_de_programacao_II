import calendar
from db import produtos, vendas
from utils import obter_ano_mes, criar_dicionario_produtos_por_id, calcular_vendas_por_mes_ano

def processar_vendas():
    # Obtém o ano e o mês digitados pelo usuário
    ano_digitado, mes_digitado = obter_ano_mes()

    # Cria um dicionário com os produtos mapeados por ID
    produtos_por_id = criar_dicionario_produtos_por_id(produtos)

    try:
        # Calcula as vendas totais e produtos vendidos no mês e ano informados
        total_vendas, produtos_vendidos = calcular_vendas_por_mes_ano(vendas, ano_digitado, mes_digitado)

        # Obtém o produto mais vendido
        if produtos_vendidos:
            # Encontra o ID do produto mais vendido usando a função max() com base na quantidade vendida
            produto_mais_vendido_id = max(produtos_vendidos, key=produtos_vendidos.get)
            # Obtém o nome do produto mais vendido com base no ID usando o dicionário de produtos por ID
            produto_mais_vendido_nome = produtos_por_id.get(produto_mais_vendido_id)
            # Obtém a quantidade vendida do produto mais vendido usando o dicionário de produtos vendidos
            quantidade_produto_mais_vendido = produtos_vendidos[produto_mais_vendido_id]
            # Imprime as informações do produto mais vendido
            print(f"\nProduto mais vendido: {produto_mais_vendido_nome}, \nQuantidade vendida do produto: {quantidade_produto_mais_vendido}\n")
        else:
            # Caso não haja produtos vendidos no mês e ano informados, imprime uma mensagem informando isso
            print("Não foram encontrados produtos vendidos no mês e ano informados.")

        # Imprime o total de vendas para o mês e ano informados
        print(f"Total de vendas para o mês {mes_digitado}/{ano_digitado}: R${total_vendas:.2f}\n")

        # Calcula a média de vendas por dia
        # Obtém o último dia do mês com base no ano e mês de referência usando a função monthrange() do módulo calendar
        ultimo_dia_mes = calendar.monthrange(ano_digitado, mes_digitado)[1]
        # Calcula a média de vendas por dia dividindo o total de vendas pelo número de dias no mês
        media_vendas_por_dia = total_vendas / ultimo_dia_mes
        # Imprime a média de vendas por dia
        print(f"Média de vendas por dia: R${media_vendas_por_dia:.2f}\n")
    except ValueError:
        # Caso ocorra uma exceção ao calcular as vendas (por exemplo, se o mês ou ano informados não possuírem vendas), imprime uma mensagem de erro
        print("Não há vendas registradas para o mês e ano informados.\n")

