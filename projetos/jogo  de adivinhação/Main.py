import random

print("JOGO DE ADIVINHAÇÃO")
print("")
print("OlA JOGADOR")
print("")
print("O jogo vai selecionar um numero de 1 até 100, tente adinhar qual é")
print("")
print("O jogo ira te dar dicas se o numero selecionado pelo jogo é maior ou menor que o numero que você chutou")
print("")

sair = 0
numero_aleatorio = random.randint(1, 100)

while True:
    try:
        chute = int(input("digite o seu chute: "))
        if chute >= 1 and chute <= 100:
            break
        else:
          print("invalido digite um numero entre 1 e 100")
    except ValueError:
        print("digite apenas numeros")


while chute != sair:

    if chute > numero_aleatorio:
        print("esse numero é maior do que o jogo escolheu")
        print("")

    elif chute < numero_aleatorio:
        print("esse numero é menor do que o jogo escolheu")
        print("")

    else:
       print("")
       print("Parabens você acertou o numero\n digite 0 se quiser sair do jogo\n se quiser continuar faça o seu proximo chute")
       print("")

        while True:
            try:
                replay = int(input("digite se você quer jogar novamente: (s/n) "))
                if replay == "s":
                    numero_aleatorio = random.randint(1, 100)
                    break
                else:
                    print("invalido digite um numero entre 1 e 100")
            except ValueError:
                print("digite apenas numeros")

    while True:
        try:
            chute = int(input("digite o seu chute: "))
            if chute >= 1 and chute <= 100 :
                break
            else:
                print("invalido digite um numero entre 1 e 100")
        except ValueError:
            print("digite apenas numeros")