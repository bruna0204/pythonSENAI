print("coloque a temperatura em graus Celsius para exibirmos o valor em graus Fahrenheit e kelvin.")




def solicita_temperatura():
    while True:
        try:
          temperatura_em_celsios = int(input("digite aqui a temperatura em graus Celsius: "))
          return temperatura_em_celsios
        except ValueError:
            print("digite apenas numeros")


def exibir_kelvin(temperatura_em_celsios):
    kelvin = temperatura_em_celsios + 273.15
    print(f'o valor em kelvin é {kelvin}')


def exibir_fahrenheit(temperatura_em_celsios):
    fahrenheit = temperatura_em_celsios * 1.8 + 32
    print(f'o valor em fahrenheit é {fahrenheit}')


temperatura = solicita_temperatura()


exibir_kelvin(temperatura)


exibir_fahrenheit(temperatura)


