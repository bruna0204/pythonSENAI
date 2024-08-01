import random #sorteio

print("JOGO DO PAR OU IMPAR")
print("")
print("OLA JOGADOR")
print("")
print("Para começar escolha entre par ou impar\nDepois digite um numero de 0 até 5\nE exibiremos em quem ganhou ")
print("")


numero_aleatorio = random.randint(0, 5)


while True:
    try:
        escolha = input("Escolha par ou impar: ")
        if escolha == "par" or escolha == "impar":
            break
        else:
          print("inválido, digite apenas impar ou par")
    except ValueError:
        print("digite apenas letras")


print("")


while True:
    try:
        numero = int(input("Digite um numero de 0 a 5: "))
        if numero >= 0 and numero <= 5:
            break
        else:
            print("inválido, digite um numero entre 0 e 5")
    except ValueError:
         print("inválido, digite apenas numeros")


print("")

valor_da_soma = numero_aleatorio + numero
print(valor_da_soma)

sair = ""
pares = valor_da_soma % 2


while sair != "não":
    valor_da_soma = numero_aleatorio + numero
    if pares == 0:
       if escolha == "par":
           print(f"parabens você venceu {valor_da_soma}, é par")
       else:
           print("é par, você perdeu")

    else:
        if escolha == "impar":
            print(f"parabens você venceu,{valor_da_soma} é impar")
        else:
            print("é impar, você perdeu")
    sair = input("Deseja continuar sim ou não? ")
    if sair == "sim":
        numero_aleatorio = random.randint(0, 5)

        while True:
            try:
                escolha = input("Escolha par ou impar: ")
                if escolha == "par" or escolha == "impar":
                    break
                else:
                    print("inválido, digite apenas impar ou par")
            except ValueError:
                print("digite apenas letras")

        print("")

        while True:
            try:
                numero = int(input("Digite um numero de 0 a 5: "))
                if numero >= 0 and numero <= 5:
                    break
                else:
                    print("inválido, digite um numero entre 0 e 5")
            except ValueError:
                print("inválido, digite apenas numeros")










