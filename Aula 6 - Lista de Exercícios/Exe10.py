# 10) Escreva um programa para ler um número de unidade de comprimento (um fracionário) 
#     e mostre a área do círculo deste raio. Assuma como valor do pi 3.14159 (uma apropriada
#     declaração deve ser dada a esta constante). A saída deveria ter a seguinte forma:
#     A área do círculo de raio ___ unidades e ___ unidades.
#     Se você desejar melhorar este código, exiba a mensagem: Erro: valores negativos não são
#     permitidos. Se o valor de entrada for negativo.

import math

print("Programa para calcular a área de um círculo")

PI = 3.14159

raio_do_circulo = float(input("Informe o comprimento do raio do círculo em centimetros: "))

while (raio_do_circulo < 0):
    print("Não é possível realizar o cálculo com valores negativos, por favor informe um número igual ou maior que zero")
    raio_do_circulo = float(input("Informe o comprimento do raio do círculo em centimetros: "))

area_do_circulo = PI * math.pow(raio_do_circulo, 2)

print(f"A área do círculo de raio {raio_do_circulo:.2f} cm é {area_do_circulo:.2f} cm")
   


