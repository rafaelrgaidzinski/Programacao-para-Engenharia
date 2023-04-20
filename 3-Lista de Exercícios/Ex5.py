#   3) Escreva um programa que pede o raio de um círculo, e em seguida exiba o perímetro
#   e área do círculo.

import math

print("Programa para calcular a área e o perímetro de um círculo")

raio_do_circulo = float(input("Informe o raio do círculo: "))

perimetro = 2 * math.pi * raio_do_circulo
perimetro = round(perimetro, 2)

area = math.pi * (math.pow(raio_do_circulo, 2))
area = round(area, 2)

print("Perímetro do círculo: " + str(perimetro), "Área do círculo: " + str(area), sep="\n")