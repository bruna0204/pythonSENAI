while True:
    try: #tentar execucutar
        chute = int(input("digite o seu chute: "))
        if chute >= 1 and chute <= 100:
            #verifica e valida
            break #parar o while
        else:
          print("invalido digite um numero entre 1 e 100")
    except ValueError:
        #caso de erro execute aqui
        print("digite apenas numeros")
