print("selcione o numero para calcular a resistencia ou tensão ou a corrente eletrica ou resistência resistor:")
print("")
print("1 - resistencia\n2 - tesao\n3 - corrente\n4 - resistencia resistor\n0 - sair ")
print("")
resistencia = 1
tensao = 2
corrente = 3
resistencia_resistor = 4
sair = 0


selecao = int(input("digite o que você deseja calcular: "))

while selecao != 0:
    if selecao == resistencia:
        print("resistencia")
        print("")

        while True:
            try:
                tensao = float(input("qual a tensão Elétrica em V: "))
                if tensao >0:
                    break
            except ValueError:
                print("Valor inválido, digite ultilizando o ponto como separador. Ex: 1.0")


        while True:
            try:
                corrente = float(input("qual a corrente eletrica em A: "))
                if tensao >0:
                    break
            except ValueError:
                print("Valor inválido, digite ultilizando o ponto como separador. Ex: 1.0")

        valor = tensao / corrente

        print(f"o valor da resistencia é {valor} Ὡ")



    elif selecao == tensao:
      print("tensao")
      print("")
    while True:
            try:
                resistencia = float(input("qual a resistencia Eletrica em Ώ: "))
                if tensao >0:
                    break
            except ValueError:
                print("Valor inválido, digite ultilizando o ponto como separador. Ex: 1.0")

        while True:
            try:
                corrente = float(input("qual a corrente em A: "))
                if tensao >0:
                    break
            except ValueError:
                print("Valor inválido, digite ultilizando o ponto como separador. Ex: 1.0")

    conta = resistencia * corrente
        print(f"o valor da tensao é {conta} V")

      elif selecao == corrente:
         tensao = float(input("qual a tensao eletrica em V: "))
        resistencia = float(input("qual a resistencia Eletrica Ώ: "))
        resultado = tensao / resistencia
        print(f"o valor da corrente eletrica é {resultado} A")

    elif selecao == resistencia_resistor:
        tensao1 = float(input("qual a tesao da fonte  em V: "))
        tensao2 = float(input("qual a tensao em V "))
        corrente = float(input("qual a corrente em A "))
        resistencia = tensao1 - tensao2
        valor_final = resistencia / corrente
        print(f"o valor é {valor_final} Ὡ")

    else:
     print("erro")

    print("")
    print("selcione outro  numero para calcular a resistencia ou tensão ou a corrente eletrica ou resistência resistor:")
    print("")
    print("1 - resistencia\n2 - tesao\n3 - corrente\n4 - resistencia resistor\n0 - sair ")
    print("")
    selecao = int(input("digite o que você deseja calcular: "))


