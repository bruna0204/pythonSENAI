print("digite tres numeros inteiros para exibirmos qual deles é o maior")
print("")

while True:
    try:
        num1 = int(input("digite primeiro numero: "))
        num2 = int(input("digite segudo numero: "))
        num3 = int(input("digite terceiro numero: "))

        if num1 > num2 and num1 > num3:
            print(f"{num1} é maior que {num2} e  {num3}")

        elif num2 > num1 and num2 > num3:
            print(f"{num2} é maior que {num1} e {num3}")

        else:
            print(f"{num3} é maior que {num2} e {num1}")
        break
    except ValueError:
        print("Por favor, digite apenas numeros")
        