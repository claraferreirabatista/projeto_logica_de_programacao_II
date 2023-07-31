import random  # Importando a biblioteca random para gerar o ID da venda

# Definindo a classe Vendedor
class Vendedor:
    def __init__(self, nome):
        self.nome = nome

# Mock de vendedores (mantemos o mesmo do exemplo anterior)
vendedores = (
    Vendedor("João"),
    Vendedor("Maria"),
    Vendedor("Pedro"),
    Vendedor("Ana")
)

# Definindo a classe Produto
class Produto:
    def __init__(self, id_produto, nome, valor):
        self.id_produto = id_produto
        self.nome = nome
        self.valor = valor

# Mock de produtos (mantemos o mesmo do exemplo anterior)
produtos = [
    Produto(101, "Smartphone Modelo X", 1500.00),
    Produto(102, "Notebook Ultra Y", 3500.00),
    Produto(103, "Smart TV 4K 50 polegadas", 2200.00),
    Produto(104, "Fone de Ouvido Sem Fio", 200.00),
    Produto(105, "Câmera DSLR Profissional", 2800.00),
    Produto(106, "Tablet Super Slim", 800.00),
    Produto(107, "Smartwatch Modelo Z", 500.00),
    Produto(108, "Impressora Multifuncional", 300.00),
    Produto(109, "Console de Videogame Next-Gen", 4000.00),
    Produto(110, "Monitor LED 27 polegadas", 900.00),
    Produto(111, "Teclado Gamer RGB", 150.00),
    Produto(112, "Mouse Sem Fio Recarregável", 80.00),
    Produto(113, "Caixa de Som Bluetooth", 120.00),
    Produto(114, "Roteador Wi-Fi Potente", 150.00),
    Produto(115, "Câmera de Segurança IP", 250.00)
]

# Definindo a classe Venda
class Venda:
    def __init__(self, venda_ID, vendedor):
        self.venda_ID = venda_ID
        self.vendedor = vendedor
        self.produtos = {}  # Dicionário que armazena os produtos e suas quantidades
        self.valor_total_da_venda = 0

    # Método para adicionar produtos à venda
    def adicionar_produto(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if produto in self.produtos:
            self.produtos[produto] += quantidade
        else:
            self.produtos[produto] = quantidade
        self.valor_total_da_venda += produto.valor * quantidade

def validar_cpf(cpf):
    # Implementação básica de validação do CPF (apenas para fins ilustrativos)
    cpf = cpf.replace('.', '').replace('-', '')  # Remover pontos e traços, se houver
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    return True  # Retornar True se o CPF for válido

def validar_data(data):
    # Implementação básica de validação da data (apenas para fins ilustrativos)
    try:
        dia, mes, ano = map(int, data.split('/'))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100:
            return True
        else:
            return False
    except ValueError:
        return False

# Mock de vendas (mantemos o mesmo do exemplo anterior)
vendas = [
    {
       "id_venda": 1001,
        "Nome do Vendedor": vendedores[0].nome,
        "CPF do Comprador": "123.456.789-10",
        "Data da Venda": "01/07/2023",
        "Produtos": [
            {
                "produto_id": produtos[0].id_produto,
                "nome_do_produto": produtos[0].nome,
                "valor_do_produto": produtos[0].valor
            },
            {
                "produto_id": produtos[1].id_produto,
                "nome_do_produto": produtos[1].nome,
                "valor_do_produto": produtos[1].valor
            }
        ],
        "total_da_venda": (produtos[0].valor * 2) + produtos[1].valor
    },
    {
        "id_venda": 1002,
        "Nome do Vendedor": vendedores[1].nome,
        "CPF do Comprador": "987.654.321-00",
        "Data da Venda": "10/07/2023",
        "Produtos": [
            {
                "produto_id": produtos[2].id_produto,
                "nome_do_produto": produtos[2].nome,
                "valor_do_produto": produtos[2].valor
            }
        ],
        "total_da_venda": produtos[2].valor
    },
    {
        "id_venda": 1003,
        "Nome do Vendedor": vendedores[2].nome,
        "CPF do Comprador": "111.222.333-44",
        "Data da Venda": "15/07/2023",
        "Produtos": [
            {
                "produto_id": produtos[3].id_produto,
                "nome_do_produto": produtos[3].nome,
                "valor_do_produto": produtos[3].valor
            },
            {
                "produto_id": produtos[4].id_produto,
                "nome_do_produto": produtos[4].nome,
                "valor_do_produto": produtos[4].valor
            },
            {
                "produto_id": produtos[5].id_produto,
                "nome_do_produto": produtos[5].nome,
                "valor_do_produto": produtos[5].valor
            }
        ],
        "total_da_venda": (produtos[3].valor + produtos[4].valor + produtos[5].valor)
    },
     {
        "id_venda": 1004,
        "Nome do Vendedor": vendedores[0].nome,
        "CPF do Comprador": "555.666.777-88",
        "Data da Venda": "20/07/2023",
        "Produtos": [
            {
                "produto_id": produtos[6].id_produto,
                "nome_do_produto": produtos[6].nome,
                "valor_do_produto": produtos[6].valor
            },
            {
                "produto_id": produtos[7].id_produto,
                "nome_do_produto": produtos[7].nome,
                "valor_do_produto": produtos[7].valor
            },
            {
                "produto_id": produtos[8].id_produto,
                "nome_do_produto": produtos[8].nome,
                "valor_do_produto": produtos[8].valor
            }
        ],
        "total_da_venda": (produtos[6].valor + produtos[7].valor + produtos[8].valor)
    },
    {
        "id_venda": 1005,
        "Nome do Vendedor": vendedores[1].nome,
        "CPF do Comprador": "999.888.777-66",
        "Data da Venda": "25/07/2023",
        "Produtos": [
            {
                "produto_id": produtos[9].id_produto,
                "nome_do_produto": produtos[9].nome,
                "valor_do_produto": produtos[9].valor
            },
            {
                "produto_id": produtos[10].id_produto,
                "nome_do_produto": produtos[10].nome,
                "valor_do_produto": produtos[10].valor
            }
        ],
        "total_da_venda": (produtos[9].valor + produtos[10].valor)
    },
     {
        "id_venda": 1006,
        "Nome do Vendedor": vendedores[3].nome,
        "CPF do Comprador": "777.888.999-00",
        "Data da Venda": "01/08/2023",
        "Produtos": [
            {
                "produto_id": produtos[11].id_produto,
                "nome_do_produto": produtos[11].nome,
                "valor_do_produto": produtos[11].valor
            },
            {
                "produto_id": produtos[12].id_produto,
                "nome_do_produto": produtos[12].nome,
                "valor_do_produto": produtos[12].valor
            }
        ],
        "total_da_venda": (produtos[11].valor + produtos[12].valor)
    },
    {
        "id_venda": 1007,
        "Nome do Vendedor": vendedores[2].nome,
        "CPF do Comprador": "333.444.555-66",
        "Data da Venda": "05/08/2023",
        "Produtos": [
            {
                "produto_id": produtos[3].id_produto,
                "nome_do_produto": produtos[3].nome,
                "valor_do_produto": produtos[3].valor
            }
        ],
        "total_da_venda": produtos[3].valor
    },
    {
        "id_venda": 1008,
        "Nome do Vendedor": vendedores[0].nome,
        "CPF do Comprador": "999.111.222-33",
        "Data da Venda": "10/08/2023",
        "Produtos": [
            {
                "produto_id": produtos[5].id_produto,
                "nome_do_produto": produtos[5].nome,
                "valor_do_produto": produtos[5].valor
            },
            {
                "produto_id": produtos[6].id_produto,
                "nome_do_produto": produtos[6].nome,
                "valor_do_produto": produtos[6].valor
            }
        ],
        "total_da_venda": (produtos[5].valor + produtos[6].valor)
    }
]

# Imprimindo o mock de vendas
for venda in vendas:
    print(f"Venda ID: {venda['id_venda']}")
    print(f"Nome do Vendedor: {venda['Nome do Vendedor']}")
    print(f"CPF do Comprador: {venda['CPF do Comprador']}")
    print(f"Data da Venda: {venda['Data da Venda']}")
    print("Produtos:")
    for produto in venda['Produtos']:
        print(f"- Produto ID: {produto['produto_id']}")
        print(f"  Nome do Produto: {produto['nome_do_produto']}")
        print(f"  Valor do Produto: R$ {produto['valor_do_produto']:.2f}")
    print(f"Total da Venda: R$ {venda['total_da_venda']:.2f}\n")

while True:
    resposta = input("Deseja criar uma venda? (s/n): ").lower()
    if resposta not in {'s', 'sim'}:
        break

    venda_ID = random.randint(1000, 9999)
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
            for produto, quantidade in nova_venda.produtos.items()  # Correção do método items() no lugar de values()
        ],
        "total_da_venda": nova_venda.valor_total_da_venda
    })

    resposta = input("Deseja realizar outra venda? (s/n): ").lower()
    if resposta not in {'s', 'sim'}:
        break

print("Vendas realizadas:")
for venda in vendas:
    print(f"Venda ID: {venda['id_venda']}")
    print(f"Nome do Vendedor: {venda['Nome do Vendedor']}")
    print(f"CPF do Comprador: {venda['CPF do Comprador']}")
    print(f"Data da Venda: {venda['Data da Venda']}")
    print("Produtos:")
    for produto in venda['Produtos']:
        print(f"- Produto ID: {produto['produto_id']}")
        print(f"  Nome do Produto: {produto['nome_do_produto']}")
        print(f"  Valor do Produto: R$ {produto['valor_do_produto']:.2f}")
    print(f"Total da Venda: R$ {venda['total_da_venda']:.2f}\n")
    print()

def excluir_venda_por_id(id_venda):
    global vendas  # Permite que a função acesse a variável global 'vendas'
    for i, venda in enumerate(vendas):
        if venda['id_venda'] == id_venda:
            del vendas[i]
            return True
    return False

while True:
    resposta = input("Deseja excluir uma venda? (s/n): ").lower()
    if resposta not in {'s', 'sim'}:
        break

    id_venda_excluir = int(input("Digite o ID da venda que deseja excluir: "))
    if excluir_venda_por_id(id_venda_excluir):
        print(f"Venda com ID {id_venda_excluir} excluída com sucesso.")
    else:
        print(f"Venda com ID {id_venda_excluir} não encontrada.")

print("Obrigada por usar o programa!")

from datetime import datetime

# Função para converter a data digitada pelo usuário em formato de string para formato de data
def converter_data(data_str):
    return datetime.strptime(data_str, '%d/%m/%Y').date()

# Função para encontrar o vendedor com mais vendas e o produto mais vendido do mês e ano fornecidos
def encontrar_melhor_vendedor_e_produto(vendas, ano, mes):
    # Converter a data do usuário para o mesmo formato das datas na lista de vendas
    data_procurada = converter_data(f'01/{mes}/{ano}')

    # Filtrar as vendas que correspondem ao mês e ano fornecidos pelo usuário
    vendas_do_mes = [venda for venda in vendas if converter_data(venda["Data da Venda"]) == data_procurada]

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

melhor_vendedor, total_vendas_melhor_vendedor, produto_mais_vendido, quantidade_total_produto_mais_vendido = encontrar_melhor_vendedor_e_produto(vendas, ano_escolhido, mes_escolhido)

print(f"Melhor vendedor do mês {mes_escolhido}/{ano_escolhido}: {melhor_vendedor}, Total de vendas: R${total_vendas_melhor_vendedor:.2f}")
print(f"Produto mais vendido do mês {mes_escolhido}/{ano_escolhido}: {produto_mais_vendido}, Quantidade total vendida: R${quantidade_total_produto_mais_vendido:.2f}")
