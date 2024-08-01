print("coloque o ano do seu nascimento para verificar se você é maior ou menor de idade")
print("")
while True:
    try:
        ano = int(input("Digite o ano do seu nascimento: "))
        idade = 2024 - ano

        if idade >= 18:
            print(f"essa pessoa tem {idade} anos, ela é maior de idade")
        elif idade >= 122:
            print(f"essa pessoa tem {idade} anos, ela n existe atualmente")
        else:
            print(f"essa pessoa tem {idade} anos, ela é menor de idade")
        break
    except ValueError:
        print("digite apenas numeros")

