#   2) Construa um programa que receba do usuário a variação do deslocamento
#   de um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao
#   fim, o programa deve calcular a velocidade média, em m/s, do objeto. Mostrar
#   os dados fornecidos e o valor calculado.

print("Programa para calcular a velocidade média em m/s")

deslocamento_em_metros = float(input("Quantos mestros o objeto se deslocou: "))
tempo_em_segundos = int(input("Quantos segundos o objeto levou para se deslocar: "))

velocidade_media = deslocamento_em_metros / tempo_em_segundos
velocidade_media = round(velocidade_media, 2)

print("Deslocamento em metros: " + str(deslocamento_em_metros), "Tempo em segundos: " + str(tempo_em_segundos),
        "Velocidade média: " + str(velocidade_media) + " m/s", sep="\n")


