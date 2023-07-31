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

Entendido! Vamos criar um planejamento para o projeto de Data Science da loja que guarda todas as vendas e realiza análises para identificar os vendedores com mais vendas e os produtos mais vendidos. Faremos tudo em Python e atenderemos aos requisitos especificados.

**Passo a passo do projeto:**

1. **Definir a estrutura de dados:**
   - Criar classes para representar os objetos venda, vendedor e produto.
   - Implementar a estrutura de lista para armazenar todas as vendas.

2. **Criar o banco de dados mock para os produtos disponíveis:**
   - Criar um dicionário onde as chaves serão os IDs dos produtos e os valores serão objetos que contêm as informações do produto (nome, valor, etc.).

3. **Função para gerar IDs aleatórios de venda e produto:**
   - Criar uma função para gerar IDs aleatórios com 4 e 5 dígitos para venda e produto, respectivamente.

4. **Função para incluir novas vendas:**
   - Criar uma função para permitir ao usuário incluir novas vendas.
   - Solicitar ao usuário todos os campos necessários para criar uma venda (nome do vendedor, CPF do comprador, data, etc.).
   - Tratar possíveis erros de preenchimento incorreto.

5. **Função para incluir produtos em uma venda:**
   - Após criar a venda, solicitar ao usuário o ID do produto e a quantidade que deseja incluir.
   - Buscar as informações do produto no banco de dados mock e adicionar à venda.

6. **Implementar estrutura de controle para inclusão de múltiplos produtos:**
   - Permitir ao usuário incluir vários produtos na mesma venda, repetindo a ação até que ele indique que não deseja mais incluir.

7. **Função para acessar vendas por ano e mês:**
   - Criar uma função para que o usuário informe o ano e o mês desejado.
   - Exibir todas as vendas realizadas naquele mês e ano específicos.

8. **Análise das vendas por vendedor:**
   - Calcular o rendimento do vendedor para um determinado mês.
   - Identificar o vendedor que realizou mais vendas naquele mês.

9. **Análise das vendas por produto:**
   - Somar as vendas de cada produto para um determinado mês.
   - Identificar os três produtos mais vendidos naquele mês.

10. **Opção para excluir vendas:**
    - Criar uma opção para o usuário excluir vendas do banco de dados.

11. **Opção para excluir produtos de uma venda:**
    - Criar uma opção para o usuário remover produtos de uma venda já realizada.

12. **Menu principal e interface de interação com o usuário:**
    - Criar um menu para que o usuário escolha as opções disponíveis (incluir venda, acessar vendas, excluir venda, etc.).
    - Implementar uma interface amigável para guiar o usuário durante as interações.

Com esse planejamento, teremos um projeto bem estruturado para uma loja que realiza vendas e armazena todas as informações necessárias para análises de vendas por vendedor, produto e período específico. O projeto será bastante detalhado e lógico, atendendo aos requisitos de um desenvolvedor iniciante em Data Science utilizando apenas Python sem bibliotecas externas.