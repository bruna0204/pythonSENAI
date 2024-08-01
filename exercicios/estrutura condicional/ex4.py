print("digite dois numeros para verificar qual deles é o maior e o menor")

while True:
    try:
        numero1 = int(input("digite o primeiro numero: "))
        numero2 = int(input("digite o segundo numero: "))

        if numero1 > numero2:
            print(f"o numero {numero1} é maior que o numero {numero2}")
        else:
            print(f"o numero {numero2} é maior que o numero {numero1}")
        break
    except ValueError:
        print("por favor, digite apenas numeros")