Projeto Lógica de programação II

Nesse projeto iremos focar no conhecimento adquirido durante o módulo de lógica de programação II.

Utilizaremos as estruturas de dados (tuplas, listas, dicionários) além da lógica de programação (if/else, while, e for), lembre-se das compreensões de listas e dicionários. E utilize as técnicas e algoritmos que achar necessário para realizar o projeto. A ideia é que no projeto sejam utilizados o maior número possível de recursos que foram aprendidos durante o módulo.

Critérios de avaliação
Os seguintes itens serão avaliados:

Reprodutibilidade do código: seu código será executado e precisa gerar os mesmos resultados apresentados por você;

Clareza: seu código precisa ser claro e deve existir uma linha de raciocínio direta. Comente o código em pontos que julgar necessário para o entendimento total;

Utilização dos recursos aprendidos durante o módulo.

Informações gerais
O projeto pode ser desenvolvido individualmente ou em grupo

Entrega (em definição).

Anexar, na entrega, o código (notebook ou script python) desenvolvido e os arquivos gerados.

Nesse projeto você deverá desenvolver um programa que permita aceitar ações da pessoa usuária (input) para o cadastro ou exclusão de uma venda realizada por uma loja. Atenção: Em uma venda, podemos ter mais de um produto vendido. Caso a venda seja excluída, registrar a informação "Venda cancelada".

Tarefas:
1.Criar uma estrutura de dados que armazene as vendas realizadas em uma loja.
Criação de objeto que conste a venda. E todas a informações necessário.
Cria uma lista de obejtos(vendas)
ex:
venda =  {
        "ID": 1,
        "Nome do produto": "Celular",
        "Valor do produto": 1500.00,
        "Nome do vendedor": "João",
        "CPF do comprador": "123.456.789-00",
        "Data da venda": "2023-07-30",
        "Informações opcionais": "Frete incluso"
    }


2.Implemente uma função que solicite ao usuário a ação desejada (Incluir ou Excluir) um item da lista.
perguntar atraves de um input qua opção do usuario
inluir ou excluir:
se incluir cair no get de função geradora
se excluir:
busca o id da venda
exclui a venda
print item excluido

Informações sobre a venda que devem constar:

ID (incremental)
Nome do produto
Valor do produto
Nome do vendedor
CPF do comprador
Data da venda
Informações opcionais

Crie uma função que calcule o valor total e o valor médio das vendas em um determinado mês.



Crie uma função para descobrir quem foi o vendedor que obteve o maior faturamento do mês. A função deve 

Crie uma função para descobrir qual foi o produto mais vendido no mês.



Crie uma função para converter os valores dos produtos em Dólar e salvar em um novo arquivo (Utilizando Função geradora).

## Aqui está uma breve explicação de cada parte do código: ##

Vendedor class: Essa classe representa um vendedor e possui um atributo nome para armazenar o nome do vendedor.

Produto class: Essa classe representa um produto e possui três atributos: id_produto, nome e valor. Cada produto é identificado por um ID único e possui um nome e um valor associado.

Venda class: Essa classe representa uma venda e tem os seguintes atributos:

venda_ID: ID único da venda.
vendedor: Objeto da classe Vendedor, representa o vendedor responsável pela venda.
produtos: Um dicionário que armazena os produtos vendidos e suas quantidades.
valor_total_da_venda: O valor total da venda, que é calculado somando o valor dos produtos vendidos.
Além disso, a classe possui um método adicionar_produto que permite adicionar produtos à venda e atualizar o valor total da venda.

Funções de validação: Existem duas funções de validação no código, validar_cpf e validar_data, que são usadas para verificar a validade de um CPF e de uma data, respectivamente. Essas funções são usadas para garantir que os dados inseridos pelo usuário durante a criação de uma nova venda sejam válidos.

Mock de vendedores, produtos e vendas: No início do código, existem mocks (dados fictícios) de vendedores, produtos e vendas para fins de exemplo. Isso permite que o código tenha algumas informações de vendas predefinidas para simular um cenário real.

Criação de novas vendas: O código permite que o usuário crie novas vendas interativamente. Ele solicita informações como o nome do vendedor, CPF do comprador, data da venda e os produtos vendidos, verificando se as entradas são válidas antes de adicionar a venda à lista de vendas.

Exclusão de vendas: O código também permite que o usuário exclua uma venda existente informando o ID da venda.

Impressão das vendas: Ao final do código, ele imprime todas as vendas registradas, incluindo as novas vendas criadas pelo usuário.