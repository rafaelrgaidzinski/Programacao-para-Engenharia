import math

print("Programa para calcular o valor final de um investimento")

valor_inicial = float(input("Informe qual o valor inicial será investido: "))
rentabilidade_mensal = float(input("Informe qual o valor da rentabilidade mensal: "))
quantidade_meses = int(input("Informe quantos meses o valor investido vai ficar aplicado: "))

rentabilidade_mensal = (1 + (rentabilidade_mensal / 100))
valor_final = valor_inicial * math.pow(rentabilidade_mensal, quantidade_meses)

print("O valor final do investimento será de R$", round(valor_final, 2))

