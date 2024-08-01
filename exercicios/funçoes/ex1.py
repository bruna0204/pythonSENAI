import datetime

def solicita_nome():
    while True:
        try:
          nome_do_usuario = input("Digite seu nome: ")
          return nome_do_usuario
        except ValueError:
            print("digite apenas letras")

def definindo_saudacao(hora):
    if hora < 0 and hora > 5:
        saudacao = "boa madrugada"
    elif hora >= 5 and hora < 12:
        saudacao = "bom dia"
    elif hora >= 12 and hora < 19:
        saudacao = "boa tarde"
    else:
        saudacao = "boa noite"
    return saudacao

tempo = datetime.datetime.now()
hora = tempo.hour

nome_do_usuario = solicita_nome()



print("ola", nome_do_usuario, definindo_saudacao(hora))