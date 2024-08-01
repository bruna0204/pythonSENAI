from Utils import *

while True:
    menu_calculadora()
    escolha_final = definindo_escolha()
    if escolha_final == 0:
        break
    else:
        exibe_resultados(escolha_final)