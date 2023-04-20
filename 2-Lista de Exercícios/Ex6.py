#   2) Ainda sobre juros compostos: Um cliente pediu que o sistema do banco tivesse a seguinte função:
#   Informar o valor inicial que ele deve investir, para ao final de 'm' meses ele tenha
#   um valor 'vf', supondo que este dinheiro esteja com uma rentabilidade 'i' mensal, em porcentagem.
#   Faça um programa que pede o valor final, o número de meses que vai ficar aplicado,
#   a rentabilidade e o script mostre o valor inicial que ele deve investir para atingir tal objetivo.

import math

print("Programa para informar o valor inicial a ser investido para atingir um objetivo de investimento")

valor_final = float(input("Informe o valor final que tem como objetivo: "))
rentabilidade_mensal = float(input("Informe a rentabilidade mensal do investimento: "))
quantidade_meses = int(input("Informe quantos meses o valor vai ficar investido: "))

rentabilidade_mensal = 1 + (rentabilidade_mensal / 100)
valor_inicial = valor_final / math.pow(rentabilidade_mensal, quantidade_meses)

print("O valor inicial a ser investido para atingir o objetivo deve ser R$", round(valor_inicial, 2))

