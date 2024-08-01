print("digite um numero para verificar se é pocitivo ou negativo")
print("")

while True:
    try:
      numero = int(input("digite o numero: "))
      if numero < 0:
         print(f"o numero {numero} é negativo")
      elif numero > 0:
          print(f"o numero {numero} é positivo")
      break
    except ValueError:
         print("inválido, digite apenas numeros")