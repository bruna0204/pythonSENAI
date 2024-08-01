print("insera tres numeros que serão os lados de um triângulo e retornaremos se ele é equilátero, isósceles ou escaleno")


def primeiro_numero():
    while True:
        try:
            lado1 = float(input("Digite o primeiro numero: "))
            return lado1
        except ValueError:
            print("digite apenas numeros")


def segundo_numero():
    while True:
        try:
            lado2 = float(input("Digite o segundo numero: "))
            return lado2
        except ValueError:
            print("digite apenas numeros")


def terceio_numero():
    while True:
        try:
            lado3 = float(input("Digite o terceiro numero: "))
            return lado3
        except ValueError:
            print("digite apenas numeros")


def identicacao_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print("Os lados são iguais, esse é um triangulo equilatero")

    elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado2 != lado1 or lado2 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
        print("tem um lado diferente, esse triangulo é esosceles")

    else:
        print("tem lados diferentes, esse triangulo é um escaleno")

print("")
numero1 = primeiro_numero()
numero2 = segundo_numero()
numero3 = terceio_numero()

identicacao_triangulo(numero1, numero2, numero3)