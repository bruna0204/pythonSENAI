
def menu_calculadora():
    print("selecione o numero para calcular a resistencia ou tensão ou a corrente eletrica ou resistência resistor:")
    print("")
    print("1 - resistencia\n2 - tesao\n3 - corrente\n4 - resistencia resistor\n0 - sair ")
    print("")


def definindo_escolha():
    while True:
        try:
            selecao = int(input("digite o que você deseja calcular: "))
            if selecao >= 0 and selecao <= 4:
                return selecao
            else:
                print("digite um numero entre 0 e 4")
        except ValueError:
            print("digite apenas numeros ")


def solicita_tensao():
    while True:
        try:
            tensao = float(input("qual a tensão Elétrica em V: "))
            if tensao > 0:
                return tensao
        except ValueError:
            print("Valor inválido, digite ultilizando o ponto como separador. Ex: 1.0")


def solicita_corrente():
    while True:
        try:
            corrente = float(input("qual a corrente eletrica em A: "))
            if corrente > 0:
                return corrente
        except ValueError:
            print("Valor inválido, digite ultilizando o ponto como separador. Ex: 1.0")


def solicita_resistencia():
    while True:
            try:
                resistencia = float(input("qual a resistencia Eletrica em Ώ: "))
                if resistencia >0:
                    return resistencia
            except ValueError:
                print("Valor inválido, digite ultilizando o ponto como separador. Ex: 1.0")


def solicita_tensao_da_fonte():
    while True:
        try:
            tensao1 = float(input("qual a tesao da fonte  em V: "))
            if tensao1 > 0:
                return tensao1
        except ValueError:
            print("Valor inválido, digite ultilizando o ponto como separador. Ex: 1.0")


def conta_resistencia(tensao, corrente):
    return tensao / corrente


def conta_tensao(resistencia, corrente):
    return resistencia * corrente


def conta_corrente(tensao, resistencia):
    return tensao / resistencia


def resistencia_resistor(solicita_tensao_da_fonte, tensao, corrente):
    return (tensao - solicita_tensao_da_fonte) / corrente


def exibe_resultados(selecao):
    if selecao == 1:
        print("resistencia eletrica")
        tensao1 = solicita_tensao()
        corrente1 = solicita_corrente()
        print(conta_resistencia(tensao1, corrente1))

    elif selecao == 2:
        print("tensao")
        resistencia1 = solicita_resistencia()
        corrente1 = solicita_corrente()
        print(conta_tensao(resistencia1, corrente1))

    elif selecao == 3:
        print("")
        tensao1 = solicita_tensao()
        resistencia1 = solicita_resistencia()
        print(conta_corrente(tensao1, resistencia1))

    else:
        tensao1 = solicita_tensao()
        tensao2 = solicita_tensao_da_fonte()
        corente1 = solicita_corrente()
        print(resistencia_resistor(tensao2, tensao1, corente1))
