## EM DESENVOLVIMENTO
![image](https://github.com/claraferreirabatista/projeto_logica_de_programacao_II/assets/117992801/484ca002-0562-42af-8089-6571fe4d2ebf)

# Projeto Python - Sistema de Gerenciamento de Vendas

## Funcionamento

O sistema é composto por três classes principais:

1. **Vendedor**: Representa um vendedor com seu nome.

2. **Produto**: Representa um produto com um ID, nome e valor.

3. **Venda**: Representa uma venda, contendo um ID da venda, o vendedor responsável, os produtos vendidos e o valor total da venda.

Além disso, o sistema possui algumas funções auxiliares:

- `validar_cpf(cpf)`: Função básica para validar o formato de um CPF.
- `validar_data(data)`: Função básica para validar o formato de uma data no padrão "dd/mm/aaaa".
- `converter_data(data_str)`: Função para converter uma data no formato de string para o formato de data.
- `excluir_venda_por_id(id_venda)`: Função para excluir uma venda pelo seu ID.

### Listagem de Vendas

O programa inicia imprimindo uma lista de vendas existentes, cada uma identificada pelo seu ID, nome do vendedor, CPF do comprador, data da venda, produtos vendidos e o total da venda.

### Criar uma Nova Venda

Em seguida, o programa pergunta se deseja criar uma nova venda. Caso a resposta seja afirmativa, o usuário é solicitado a fornecer os dados da venda, incluindo o nome do vendedor, CPF do comprador, data da venda e os produtos vendidos. O sistema também valida o CPF e a data fornecida pelo usuário.

O usuário pode inserir um ou mais produtos na venda, sendo necessário informar o ID do produto e a quantidade desejada. O sistema verifica se o produto existe na lista de produtos carregados anteriormente.

### Excluir uma Venda Existente

Após a criação ou listagem das vendas, o sistema pergunta se o usuário deseja excluir uma venda. Se a resposta for afirmativa, o usuário deve fornecer o ID da venda que deseja excluir. O sistema buscará a venda correspondente pelo ID e, se encontrada, a excluirá da lista de vendas.

### Encontrar o Melhor Vendedor e Produto Mais Vendido

Ao final, o sistema pergunta ao usuário o ano e o mês para os quais deseja encontrar o melhor vendedor e o produto mais vendido. Em seguida, ele realiza uma busca nas vendas existentes e mostra o vendedor com o maior valor total de vendas no período e o produto mais vendido no mesmo período, juntamente com o valor total de vendas desse produto.

## Como Usar

Para utilizar o Sistema de Gerenciamento de Vendas, você precisará do Python instalado em sua máquina. Clone este repositório e execute o arquivo principal do projeto.

```bash
git clone https://github.com/claraferreirabatista/projeto_logica_de_programacao_II.git
cd projeto_logica_de_programacao_II
python index.py
```

O programa irá guiá-lo através das opções disponíveis e solicitará as informações necessárias para cada funcionalidade.

## Requisitos

- Python 3.x

## Contribuições

Contribuições para melhorias e correções são bem-vindas! Sinta-se à vontade para enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT license](LICENSE).