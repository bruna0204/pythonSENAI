# print(" insira dois numeros para efetuarmos uma adição, subtração, adição e multiplicação")


def menu_calculadora():
    print("calculadora")
    print("1 - soma\n2 - subtração\n3- multiplicação\n4 - divisão\n5 - todas as contas")


def escolha():
    while True:
        try:
            escolha1 = int(input("Insira sua escolha: "))
            if escolha1 >= 0 and escolha1 <= 5:
                return escolha1
            else:
                print("ivalido digite numero entre 1 e 4")
        except ValueError:
            print("digite apenas numeros")


def primeiro_numero():
    while True:
        try:
            numero1 = float(input("Insira o primeiro numero: "))
            return numero1
        except ValueError:
            print("digite apenas numeros")


def segundo_numero():
    while True:
        try:
            numero2 = float(input("Insira o segundo numero: "))
            return numero2
        except ValueError:
            print("digite apenas numeros")


def soma(numero1, numero2):
    return numero1 + numero2


def subtracao(numero1, numero2):
    return numero1 - numero2


def multiplicacao(numero1, numero2):
    return numero1 * numero2


def divisao(numero1, numero2):
    return numero1 / numero2


def operacoes_basica(escolha1, numero1, numero2):
    if escolha1 == 1:
        print(soma(numero1, numero2))

    elif escolha1 == 2:
        print(subtracao(numero1, numero2))

    elif escolha1 == 3:
        print(multiplicacao(numero1, numero2))

    elif escolha1 == 4:
        print(divisao(numero1, numero2))

    elif escolha1 == 5:
        print("soma: ", soma(numero1, numero2))
        print("subtração: ", subtracao(numero1, numero2))
        print("multiplicação: ", multiplicacao(numero1, numero2))
        print("divisão: ", divisao(numero1, numero2))



print("")
menu_calculadora()
print("")

escolha_final = escolha()
numero1 = primeiro_numero()
numero2 = segundo_numero()

operacoes_basica(escolha_final, numero1, numero2)
