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
organizar a lista de obejetos por ano, depois por mês 
pegar o valor de cada comprar do mês, sumar 
printar o rendimento mensal
e o valor médio de cada mês


Crie uma função para descobrir quem foi o vendedor que obteve o maior faturamento do mês. A função deve permitir ao usuário definir o mês e o ano desejados.
crie uma função para separar anos, e meses, aproveitando a questão anterior 
input de qual mes e ano
buscar dentro da lista criada as vendas do vendedor x 
agrupa-la e cria uma lista com as vendas do vendedor
somar o rendimento mensal de cada vendedor
e cria hanking qual total de vendas maior para menor
printa os 3 primeiro  vendedores

Crie uma função para descobrir qual foi o produto mais vendido no mês.
fazer mesmo processo da questõa anterior mas agora com produto

Crie uma função para salvar os dados em um arquivo.

Crie uma função para converter os valores dos produtos em Dólar e salvar em um novo arquivo (Utilizando Função geradora).