print("incira seu peso e sua altura para calcularmos o IMC")


def peso():
    while True:
        try:
            peso1 = float(input("Informe seu peso: "))
            return peso1
        except ValueError:
            print("digite apenas numeros")


def altura():
    while True:
        try:
            altura1 = float(input("Informe sua altura: "))
            return altura1
        except ValueError:
            print("digite apenas numeros")


def imc(altura1, peso1):
    return peso1 / (altura1 * altura1)


def classificacao(imc):
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        print("normal")
    elif 24.9 <= imc < 29.9:
        print("acima do peso")
    elif 30 <= imc < 34.9:
        print("obesidade grau 1")
    elif 35 <= imc < 39.9:
        print("obesidade grau 2")
    else:
        print("obesidade grau 3")


print("")
peso2 = peso()
altura2 = altura()
imc2 = imc(altura2, peso2)

print(imc2)
classificacao(imc2)