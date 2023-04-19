import math

print("Programa para informar o valor inicial a ser investido para atingir um objetivo de investimento")

valor_final = float(input("Informe o valor final que tem como objetivo: "))
rentabilidade_mensal = float(input("Informe a rentabilidade mensal do investimento: "))
quantidade_meses = int(input("Informe quantos meses o valor vai ficar investido: "))

rentabilidade_mensal = 1 + (rentabilidade_mensal / 100)
valor_inicial = valor_final / math.pow(rentabilidade_mensal, quantidade_meses)

print("O valor inicial a ser investido para atingir o objetivo deve ser R$", round(valor_inicial, 2))

