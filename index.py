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
    print(venda)
