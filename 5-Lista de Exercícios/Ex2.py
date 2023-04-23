#   2) Construa um programa que tem como dados de entrada dois pontos
#   quaisquer no plano cartesiano: P1 e P2. Considere que P1 é definido
#   pelas coordenadas x1 e y1, enquanto P2 por x2 e y2 . O programa deve
#   calcular e escrever a distância entre os pontos P1 e P2. A fórmula que
#   calcula a distância entre os dois pontos é dada por:
#   d = √(x2 - x1)² + (y2 - y1)²

import math

print("Programa para calcular a distancia entre dois pontos no plano cartesiano")

ponto1_x = int(input("Informe o valor da coordenada x no ponto 1: "))
ponto1_y = int(input("Informe o valor da coordenada y no ponto 1: "))

ponto2_x = int(input("Informe o valor da coordenada x no ponto 2: "))
ponto2_y = int(input("Informe o valor da coordenada y no ponto 2: "))

distancia = math.sqrt(math.pow(ponto2_x - ponto1_x, 2) + math.pow(ponto2_y - ponto1_y, 2))

print(f"A distância entre o ponto P1({ponto1_x}, {ponto1_y}) e o ponto P2({ponto2_x}, {ponto2_y}) é {distancia: .2f}")