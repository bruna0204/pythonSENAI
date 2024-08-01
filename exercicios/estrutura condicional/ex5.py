print("digite um numero de 1 até 7 para ver o dia da semana correspondente")
print("")

while True:
    try:
        numero = int(input("digite um numero: "))
        if numero == 1:
            print("o numero 1 é domingo")
            break
        elif numero == 2:
            print("o numero 2 é segunda-feira")
            break
        elif numero == 3:
            print("o numero 3 é terça-feira")
            break
        elif numero == 4:
            print("o numero 4 é quarta-feira")
            break
        elif numero == 5:
            print("o numero 5 é quinta-feira")
            break
        elif numero == 6:
            print("o numero 6 é sexta-feira")
            break
        elif numero == 7:
            print("o numero 7 é sabado")
            break

        else:
            print("numero invalido digite um numero de 1 até 7")
    except ValueError:
        print("por favor, digite apenas numeros")