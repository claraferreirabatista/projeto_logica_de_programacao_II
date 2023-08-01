from add_purchase import inclui_venda
from del_purchase import exclui_venda
from best_seller import mostrar_melhores_vendedores
from utils import obter_ano_mes
from best_product import processar_vendas

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
        inclui_venda()
    elif resposta == '2':
        exclui_venda()
    elif resposta == '3':
        mostrar_melhores_vendedores()
        break
    elif resposta == '4':
        processar_vendas()
        break
    elif resposta == '5':
        print("Opção escolhida 5")
    elif resposta == '6':
        print("Opção escolhida 6")
        break
    else:
        print("Código incorreto, digite novamente")

print("Obrigado por usar o programa")
