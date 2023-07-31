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