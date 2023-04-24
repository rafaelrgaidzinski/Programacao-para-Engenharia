#   4) Elabore um código fonte que calcule a hipotenusa de um triângulo
#   retângulo, cujos catetos serão fornecidos pelo usuário.

import math

print("Programa para calcular a hipotenusa de um triângulo retângulo")

cateto_1 = float(input("Informe a medida do primeiro cateto: "))
cateto_2 = float(input("Informe a medida do segundo cateto: "))

hipotenusa = math.sqrt(math.pow(cateto_1, 2) + math.pow(cateto_2, 2))

print(f"A medida da hipotenusa é {hipotenusa: .2f}")