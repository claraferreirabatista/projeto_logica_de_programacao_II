"""
"""
from vendas import inclui_venda

while True:
    resposta = input( "Escolha as opções, digite o respectivo número da sua opção: \n 1. Incluir venda? \n 2. Excluir venda? \n 3. Qual vendedor foi mais rentável? \n 4. Qual produto foi o mais vendido? \n 5. Mostrar todas as vendas? \n 6. Sair do programa? \n "
    )
    if resposta == '1':
        print("Opção escolhida 1")
        inclui_venda()
    elif resposta == '2':
        print("Opção escolhida 2")
    elif resposta == '3':
        print("Opção escolhida 3")
    elif resposta == '4':
        print("Opção escolhida 4")
    elif resposta == '5':
        print("Opção escolhida 5")
    elif resposta == '6':
        print("Opção escolhida 6")
        break
    else:
        print("Código incorreto, digite novamente")

print("Obrigado por usar o programa")
