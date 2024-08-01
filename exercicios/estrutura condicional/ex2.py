print("coloque duas nota para calcularmos a media")
print("")
while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        soma = nota1 + nota2
        media = soma / 2

        if media > 70:
            print(f"sua media foi {media}, você foi aprovado!")

        elif media < 70:
            print(f"sua media foi {media}, você foi reprovado!")
        break
    except ValueError:
        print("invalido, digite apenas numeros")

