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