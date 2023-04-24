#   1) Desenvolva um gerador de tabuada, capaz de gerar a tabuada
#   de qualquer número inteiro entre 1 à 10. O usuário deve informar
#   de qual número ele deseja ver a tabuada.

print("Gerador de tabuada")

numero_tabuada = int(input("Informe um número para gerar a tabuada: "))

print("Tabuada de", numero_tabuada)

for multiplicador in range(1, 11):
    print(numero_tabuada, "x", multiplicador, "=", numero_tabuada * multiplicador)
