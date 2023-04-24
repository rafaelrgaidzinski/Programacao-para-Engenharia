#   1) Escreva um programa que receba 2 valores de x e y. Em seguida calcule e
#   imprima o valor de z de acordo com a fórmula: (x**2 + y**2) / (x - y)

import math

print("Programa para realizar cálculos")

valor_x = int(input("Informe o valor de x: "))
valor_y = int(input("Informe o valor de y: "))

valor_z = (math.pow(valor_x, 2) + math.pow(valor_y, 2)) / (valor_x - valor_y)

print("O valor de z é ", valor_z)