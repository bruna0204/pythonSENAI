import datetime

tempo = datetime.datetime.now()
ano = tempo.year
mes = tempo.month
#semana = tempo.weekday()
semana = tempo.strftime("%w")
hora = tempo.hour
minuto = tempo.minute
segundo = tempo.second
dia = tempo.day
#semanas = 0

print(f'TESTE: {semana}')


if tempo.month == 1:
    meses ="janeiro"

elif tempo.month == 2:
    meses = "fevereiro"

elif tempo.month == 3:
    meses = "março"

elif tempo.month == 4:
    meses = "abril"

elif tempo.month == 5:
    meses = "maio"

elif tempo.month == 6:
    meses = "junho"

elif tempo.month == 7:
    meses = "julho"

elif tempo.month == 8:
    meses = "agosto"

elif tempo.month == 9:
    meses = "setembro"

elif tempo.month == 10:
    meses = "outubro"

elif tempo.month == 11:
    meses = "novembro"

elif tempo.month == 12:
   meses = "dezembro"


if semana == 0:
   semanas = "domingo"

elif semana == 1:
    semanas = "segunda-feira"

elif semana == 2:
    semanas = "terça-feira"

elif semana == 3:
    semanas = "quarta-feira"

elif semana == 4:
    semanas = "quinta-feira"

elif semana == '5':
    semanas = "sexta-feira"

elif semana == 6:
    semanas = "sabado"


if hora < 12:
    saudacao = "bom dia"
elif hora >= 12 and hora < 18:
    saudacao = "boa tarde"
else:
    saudacao = "boa noite"
print(f"{saudacao} hoje é {semanas} dia {dia}, {meses}, {ano}, agora são {hora} horas {minuto} minutos e {segundo} segundos")







