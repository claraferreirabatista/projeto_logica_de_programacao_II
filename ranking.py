from datetime import datetime

# Função para converter a data digitada pelo usuário em formato de string para formato de data

def converter_data(data_str):
    return datetime.strptime(data_str, '%d/%m/%Y').date()

# Função para encontrar o vendedor com mais vendas e o produto mais vendido do mês e ano fornecidos

def encontrar_melhor_vendedor_e_produto(vendas, ano, mes):
    # Converter a data do usuário para o mesmo formato das datas na lista de vendas
    data_procurada = converter_data(f'01/{mes}/{ano}')

    # Filtrar as vendas que correspondem ao mês e ano fornecidos pelo usuário
    vendas_do_mes = [venda for venda in vendas if converter_data(
        venda["Data da Venda"]) == data_procurada]

    # Inicializar as variáveis para guardar as informações sobre o melhor vendedor e o produto mais vendido
    melhor_vendedor = None
    total_vendas_melhor_vendedor = 0
    produto_mais_vendido = None
    quantidade_total_produto_mais_vendido = 0

    # Iterar pelas vendas do mês para encontrar o melhor vendedor e o produto mais vendido
    for venda in vendas_do_mes:
        total_vendas_vendedor = 0

        # Calcular o total de vendas do vendedor
        for item in venda["Produtos"]:
            total_vendas_vendedor += item["valor_do_produto"]

        # Atualizar o melhor vendedor e o total de vendas do melhor vendedor, se necessário
        if total_vendas_vendedor > total_vendas_melhor_vendedor:
            melhor_vendedor = venda["Nome do Vendedor"]
            total_vendas_melhor_vendedor = total_vendas_vendedor

        # Iterar pelos produtos da venda para encontrar o produto mais vendido
        for item in venda["Produtos"]:
            quantidade_total_produto_mais_vendido += item["valor_do_produto"]
            if produto_mais_vendido is None or item["valor_do_produto"] > produto_mais_vendido["valor_do_produto"]:
                produto_mais_vendido = item

    return melhor_vendedor, total_vendas_melhor_vendedor, produto_mais_vendido["nome_do_produto"], quantidade_total_produto_mais_vendido

ano_escolhido = int(input("Digite o ano desejado: "))
mes_escolhido = int(input("Digite o mês desejado: "))

melhor_vendedor, total_vendas_melhor_vendedor, produto_mais_vendido, quantidade_total_produto_mais_vendido = encontrar_melhor_vendedor_e_produto(
    vendas, ano_escolhido, mes_escolhido)

print(
    f"Melhor vendedor do mês {mes_escolhido}/{ano_escolhido}: {melhor_vendedor}, Total de vendas: R${total_vendas_melhor_vendedor:.2f}")
print(
    f"Produto mais vendido do mês {mes_escolhido}/{ano_escolhido}: {produto_mais_vendido}, Quantidade total vendida: R${quantidade_total_produto_mais_vendido:.2f}")