#   1) Crie um programa que leia dois valores numéricos inteiros e em
#   seguida mostre um valor dentro deste intervalo, gerado aleatoriamente.

import random

print("Programa para gerar um número dentro de um intervalo numérico")

primeiro_valor = int(input("Informe o primeiro número do intervalo: "))
segundo_valor = int(input("Informe o segundo número do intervalo: "))

valor_gerado = random.randint(primeiro_valor, segundo_valor)

print("O valor gerado aleatoriamente foi o número ", valor_gerado)