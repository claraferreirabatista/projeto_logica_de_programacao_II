from add_purchase import inclui_venda
from del_purchase import exclui_venda
from best_seller import mostrar_melhores_vendedores
from utils import obter_ano_mes
from best_product import processar_vendas
from db import *

while True:
    resposta = input("""\n Escolha qual opção desejar:
    \n 1. Gostaria de incluir uma venda?
    \n 2. Ou, deseja de excluir uma venda?
    \n 3. Saber quem foram os vendores que mais venderam?
    \n 4. Ou, quer saber o nosso produto mais vendido?
    \n 5. Mostrar todas as vendas?
    \n 6. Sair do programa? \n """
                     )
    if resposta == '1':
        print("\n")
        inclui_venda()
    elif resposta == '2':
        print("\n")
        exclui_venda()
    elif resposta == '3':
        print("\n")
        mostrar_melhores_vendedores()
        break
    elif resposta == '4':
        print("\n")
        processar_vendas()
        break
    elif resposta == '5':
        print("\n")
        imprimir_vendas(vendas)
    elif resposta == '6':
        print("Opção escolhida 6")
        break
    else:
        print("Código incorreto, digite novamente")

print("Obrigado por usar o programa")
