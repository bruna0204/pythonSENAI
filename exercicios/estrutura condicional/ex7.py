print("digite um numero de 1 até 12 para ver o mes do ano correspondente")
print("")

while True:
    try:
        numero = int(input("digite um numero: "))
        if numero == 1:
            print("o numero 1 é janeiro")
            break
        elif numero == 2:
            print("o numero 2 é fevereiro")
            break
        elif numero == 3:
            print("o numero 3 é março")
            break
        elif numero == 4:
            print("o numero 4 é abril")
            break
        elif numero == 5:
            print("o numero 5 é maio")
            break
        elif numero == 6:
            print("o numero 6 é junho")
            break
        elif numero == 7:
            print("o numero 7 é julho")
            break
        elif numero == 8:
            print("o numero 8 é agosto")
            break
        elif numero == 9:
            print("o numero 9 é setembro")
            break
        elif numero == 10:
            print("o numero 10 é outubro")
            break
        elif numero == 11:
            print("o numero 11 é novembro")
            break
        elif numero == 12:
            print("o numero 12 é dezembro")

        else:
            print("numero invalido digite um numero de 1 até 12 para ver o mes do ano correspondente")
    except ValueError:
        print("por favor, digite apenas numeros")