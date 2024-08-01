from datetime import datetime

def menu_calculadora():
    print("calculadora")
    print("1 - soma\n2 - subtração\n3- multiplicação\n4 - divisão")


def return_ola_nome(nome):
    return f"ola {nome} "


def ola_nome(nome):
    print(f"Ola {nome}")


def calcular_idade(data_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - data_nascimento
    return idade


def exibir_idade(ano_de_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_de_nascimento
    print("a sua é idade ",idade, "anos")


def solicita_ano_nascimento():
    while True:
        try:
          ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
          if ano_de_nascimento > datetime.now().year:
              print("digite um ano valido")
          else:
              return ano_de_nascimento
        except ValueError:
            print("digite um valor inteiro ex: 1997")


#exibe o valor da calculadora
menu_calculadora()


#exibe o return
print(return_ola_nome("Bruna"))


ola_nome("Bruna")


print("a sua idade é", calcular_idade(data_nascimento = 1997), "anos")


exibir_idade(1997)


ano_de_nascimento = solicita_ano_nascimento()


exibir_idade(ano_de_nascimento)