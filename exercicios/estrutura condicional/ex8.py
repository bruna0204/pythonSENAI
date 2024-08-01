print("digite o seu salario bruto para calcularmos o desconto do imposto de renda")
print("")
while True:
    try:
        salario = float(input("digite o seu salario bruto: R$"))
        if salario <= 56072.00:
            print("você não desconto")

        elif salario > 56072.00 and salario <= 238532.00:
            desconto = (7.50 / 100) * salario
            print(f"o seu desconto foi de {desconto} reais")

        elif salario > 238532.00 and salario <= 522400.00:
            desconto1 = (15 / 100) * salario
            print(f"o seu desconto foi de {desconto1} reais")

        elif salario > 522400.00 and salario <= 987600.00:
            desconto2 = (22.50 / 100) * salario
            print(f"o seu desconto foi de {desconto2} reais")

        elif salario > 987600.00:
          desconto3 = (27.50 / 100) * salario
          print(f"o seu desconto foi de {desconto3} reais")
        break
    except ValueError:
        print("digite apenas numeros")