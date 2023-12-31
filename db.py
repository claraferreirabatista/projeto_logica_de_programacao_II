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

class Venda:
    def __init__(self, id_venda, vendedor):
        self.id_venda = id_venda
        self.vendedor = vendedor
        self.produtos = []
        self.valor_total_da_venda = 0

    # Método para adicionar produtos à venda
    def adicionar_produto(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self.produtos.append({"produto": produto, "quantidade": quantidade})
        self.valor_total_da_venda += produto.valor * quantidade

    # Método para retornar um iterador para os produtos da venda
    def __iter__(self):
        return iter(self.produtos)

def imprimir_vendas(vendas):
    print("==== VENDAS REALIZADAS ====\n")
    for venda in vendas:
        print(f"ID da Venda: {venda['id_venda']}")
        print(f"Vendedor: {venda['Vendedor']}")  # Correção aqui, trocar para 'Vendedor'
        print(f"CPF do Comprador: {venda['CPF do Comprador']}")
        print(f"Data da Venda: {venda['Data da Venda']}")
        print("Produtos:")
        for produto in venda['Produtos']:
            print(f"- {produto['nome_do_produto']} (Quantidade: {produto['quantidade']})")
        print(f"Total da Venda: R${venda['total_da_venda']:.2f}")
        print("============================\n")


# Mock de vendas (mantemos o mesmo do exemplo anterior)
vendas = [
    {
        "id_venda": 1001,
        "Vendedor": vendedores[0].nome,
        "CPF do Comprador": "123.456.789-10",
        "Data da Venda": "01/07/2023",
        "Produtos": [
            {
                "produto_id": produtos[0].id_produto,
                "nome_do_produto": produtos[0].nome,
                "valor_do_produto": produtos[0].valor,
                "quantidade": 2,
            },
            {
                "produto_id": produtos[1].id_produto,
                "nome_do_produto": produtos[1].nome,
                "valor_do_produto": produtos[1].valor,
                "quantidade": 1,

            },
        ],
        "total_da_venda": (produtos[0].valor * 2) + produtos[1].valor
    },
    {
    "id_venda": 1002,
    "Vendedor": vendedores[1].nome,
    "CPF do Comprador": "987.654.321-00",
    "Data da Venda": "10/07/2023",
    "Produtos": [
        {
            "produto_id": produtos[2].id_produto,
            "nome_do_produto": produtos[2].nome,
            "valor_do_produto": produtos[2].valor,
            "quantidade": 3
        }
    ],
    "total_da_venda": produtos[2].valor * 3
},
{
    "id_venda": 1003,
    "Vendedor": vendedores[2].nome,
    "CPF do Comprador": "111.222.333-44",
    "Data da Venda": "15/07/2023",
    "Produtos": [
        {
            "produto_id": produtos[3].id_produto,
            "nome_do_produto": produtos[3].nome,
            "valor_do_produto": produtos[3].valor,
            "quantidade": 2
        },
        {
            "produto_id": produtos[4].id_produto,
            "nome_do_produto": produtos[4].nome,
            "valor_do_produto": produtos[4].valor,
            "quantidade": 1
        },
        {
            "produto_id": produtos[5].id_produto,
            "nome_do_produto": produtos[5].nome,
            "valor_do_produto": produtos[5].valor,
            "quantidade": 4
        }
    ],
    "total_da_venda": (produtos[3].valor * 2) + (produtos[4].valor * 1) + (produtos[5].valor * 4)
},
{
    "id_venda": 1004,
    "Vendedor": vendedores[0].nome,
    "CPF do Comprador": "555.666.777-88",
    "Data da Venda": "20/07/2023",
    "Produtos": [
        {
            "produto_id": produtos[6].id_produto,
            "nome_do_produto": produtos[6].nome,
            "valor_do_produto": produtos[6].valor,
            "quantidade": 2
        },
        {
            "produto_id": produtos[7].id_produto,
            "nome_do_produto": produtos[7].nome,
            "valor_do_produto": produtos[7].valor,
            "quantidade": 3
        },
        {
            "produto_id": produtos[8].id_produto,
            "nome_do_produto": produtos[8].nome,
            "valor_do_produto": produtos[8].valor,
            "quantidade": 1
        }
    ],
    "total_da_venda": (produtos[6].valor * 2) + (produtos[7].valor * 3) + (produtos[8].valor * 1)
},
{
    "id_venda": 1005,
    "Vendedor": vendedores[1].nome,
    "CPF do Comprador": "999.888.777-66",
    "Data da Venda": "25/07/2023",
    "Produtos": [
        {
            "produto_id": produtos[9].id_produto,
            "nome_do_produto": produtos[9].nome,
            "valor_do_produto": produtos[9].valor,
            "quantidade": 2
        },
        {
            "produto_id": produtos[10].id_produto,
            "nome_do_produto": produtos[10].nome,
            "valor_do_produto": produtos[10].valor,
            "quantidade": 3
        }
    ],
    "total_da_venda": (produtos[9].valor * 2) + (produtos[10].valor * 3)
},
{
    "id_venda": 1006,
    "Vendedor": vendedores[3].nome,
    "CPF do Comprador": "777.888.999-00",
    "Data da Venda": "01/08/2023",
    "Produtos": [
        {
            "produto_id": produtos[11].id_produto,
            "nome_do_produto": produtos[11].nome,
            "valor_do_produto": produtos[11].valor,
            "quantidade": 1
        },
        {
            "produto_id": produtos[12].id_produto,
            "nome_do_produto": produtos[12].nome,
            "valor_do_produto": produtos[12].valor,
            "quantidade": 2
        }
    ],
    "total_da_venda": (produtos[11].valor * 1) + (produtos[12].valor * 2)
},
{
    "id_venda": 1007,
    "Vendedor": vendedores[2].nome,
    "CPF do Comprador": "333.444.555-66",
    "Data da Venda": "05/08/2023",
    "Produtos": [
        {
            "produto_id": produtos[3].id_produto,
            "nome_do_produto": produtos[3].nome,
            "valor_do_produto": produtos[3].valor,
            "quantidade": 3
        }
    ],
    "total_da_venda": produtos[3].valor * 3
},
{
    "id_venda": 1008,
    "Vendedor": vendedores[0].nome,
    "CPF do Comprador": "999.111.222-33",
    "Data da Venda": "10/08/2023",
    "Produtos": [
        {
            "produto_id": produtos[5].id_produto,
            "nome_do_produto": produtos[5].nome,
            "valor_do_produto": produtos[5].valor,
            "quantidade": 2
        },
        {
            "produto_id": produtos[6].id_produto,
            "nome_do_produto": produtos[6].nome,
            "valor_do_produto": produtos[6].valor,
            "quantidade": 1
        }
    ],
    "total_da_venda": (produtos[5].valor * 2) + (produtos[6].valor * 1)
},
{
    "id_venda": 1009,
    "Vendedor": vendedores[1].nome,
    "CPF do Comprador": "111.222.333-44",
    "Data da Venda": "15/08/2023",
    "Produtos": [
        {
            "produto_id": produtos[0].id_produto,
            "nome_do_produto": produtos[0].nome,
            "valor_do_produto": produtos[0].valor,
            "quantidade": 3
        },
        {
            "produto_id": produtos[7].id_produto,
            "nome_do_produto": produtos[7].nome,
            "valor_do_produto": produtos[7].valor,
            "quantidade": 2
        }
    ],
    "total_da_venda": (produtos[0].valor * 3) + (produtos[7].valor * 2)
},
{
    "id_venda": 1010,
    "Vendedor": vendedores[2].nome,
    "CPF do Comprador": "444.555.666-77",
    "Data da Venda": "20/08/2023",
    "Produtos": [
        {
            "produto_id": produtos[1].id_produto,
            "nome_do_produto": produtos[1].nome,
            "valor_do_produto": produtos[1].valor,
            "quantidade": 4
        },
        {
            "produto_id": produtos[8].id_produto,
            "nome_do_produto": produtos[8].nome,
            "valor_do_produto": produtos[8].valor,
            "quantidade": 1
        },
        {
            "produto_id": produtos[11].id_produto,
            "nome_do_produto": produtos[11].nome,
            "valor_do_produto": produtos[11].valor,
            "quantidade": 3
        }
    ],
    "total_da_venda": (produtos[1].valor * 4) + produtos[8].valor + (produtos[11].valor * 3)
}
]
