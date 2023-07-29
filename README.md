## EM DESENVOLVIMENTO

# Projeto Python - Sistema de Gerenciamento de Vendas

Este projeto é parte da avaliação proposta pelo curso ADA na turma de Data Science. O objetivo é desenvolver um Sistema de Gerenciamento de Vendas para uma loja, onde serão armazenadas as informações das vendas, permitindo ao usuário realizar diversas análises.

## Funcionalidades

1. **Estrutura de Dados para Armazenar Vendas**

   O projeto implementa uma estrutura de dados para armazenar as vendas realizadas na loja. Cada venda terá as seguintes informações:
   - ID (incremental)
   - Nome do produto
   - Valor do produto
   - Nome do vendedor
   - CPF do comprador
   - Data da venda

2. **Inclusão e Exclusão de Vendas**

   O sistema possui uma função que permite ao usuário realizar a inclusão ou exclusão de uma venda da lista. O usuário será solicitado a escolher a ação desejada.

3. **Cálculo do Valor Total e Médio das Vendas em um Mês**

   O projeto conta com uma função que calcula o valor total e o valor médio das vendas realizadas em um determinado mês. O usuário poderá inserir o mês desejado para realizar essa análise.

4. **Identificação do Vendedor com Maior Faturamento no Mês**

   Uma função foi implementada para descobrir qual foi o vendedor que obteve o maior faturamento em um determinado mês e ano. O usuário poderá definir o mês e o ano para realizar essa busca.

5. **Identificação do Produto Mais Vendido no Mês**

   O sistema possui uma função para identificar qual foi o produto mais vendido em um determinado mês.

6. **Salvando os Dados em um Arquivo**

   O projeto permite salvar os dados das vendas em um arquivo para armazenamento e futuras análises.

7. **Conversão dos Valores dos Produtos em Dólar**

   Há também uma função geradora para converter os valores dos produtos em Dólar e salvá-los em um novo arquivo.

## Como Usar

Para utilizar o Sistema de Gerenciamento de Vendas, você precisará do Python instalado em sua máquina. Clone este repositório e execute o arquivo principal do projeto.

```bash
git clone (https://github.com/claraferreirabatista/projeto_logica_de_programacao_II.git) [https://github.com/claraferreirabatista/projeto_logica_de_programacao_II.git]
cd projeto_logica_de_programacao_II
python main.py
```

O programa irá guiá-lo através das opções disponíveis e solicitará as informações necessárias para cada funcionalidade.

## Requisitos

- Python 3.x
- Bibliotecas: (lista das bibliotecas necessárias, caso existam)

## Contribuições

Contribuições para melhorias e correções são bem-vindas! Sinta-se à vontade para enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT license](LINCENSE) (se aplicável).
