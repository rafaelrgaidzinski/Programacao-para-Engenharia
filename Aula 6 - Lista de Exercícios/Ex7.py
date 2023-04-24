#   7) Desenvolver um programa que leia a velocidade máxima permitida em uma avenida e
#   a velocidade com que o motorista estava dirigindo por ela. Em seguida calcule o valor da
#   multa que uma pessoa receberá, sabendo que são pagos: a) R$ 85,13 se o motorista
#   ultrapassar em até 10 km/h a velocidade permitida; b) R$ 127,69 se o motorista
#   ultrapassar de 11 a 30 km/h a velocidade permitida; c) R$ 574,62 se estiver acima de 31
#   km/h da velocidade permitida. Informe também os pontos que serão inseridos na carteira
#   e o tipo de multa que será aplicado de acordo com a relação a seguir: Leve, Media e
#   Gravíssima com 3, 5 e 7 pontos, respectivamente. Caso o motorista passe dentro da
#   velocidade permitida, exibir “Vel. Normal”.

print("DETRAN - Setor Multas")

velocidade_maxima = int(input("Informe a velocidade máxima permitida na via: "))

velocidade_registrada = int(input("Informe a velocidade registrada pelo radar: "))

valor_multa = 0
tipo_multa = ""
quantidade_pontos = 0

if (velocidade_registrada <= velocidade_maxima):
    print("O motorista está dentro da velocidade permitida.")
elif (velocidade_registrada <= velocidade_maxima + 10):
    valor_multa = 85.13
    tipo_multa = "Leve"
    quantidade_pontos = 3
elif (velocidade_registrada <= velocidade_maxima + 30):
    valor_multa = 127.69
    tipo_multa = "Media"
    quantidade_pontos = 5
else:
    valor_multa = 574.62
    tipo_multa = "Gravíssima"
    quantidade_pontos = 7

if (velocidade_registrada > velocidade_maxima):
    print(f'O motorista passou {velocidade_registrada - velocidade_maxima} km/h acima da velocidade '
          f'permitida e receberá uma multa do tipo {tipo_multa} no valor de R$ {valor_multa:.2f}'
          f' e {quantidade_pontos} pontos na carteira de motorista.')