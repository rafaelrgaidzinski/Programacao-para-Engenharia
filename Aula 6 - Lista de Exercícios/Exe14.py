# 14) Criar um programa que pergunte quanto você ganha por hora e o número de horas
#     trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Programa para calcular o salário mensal")

valor_salario_por_hora = float(input("Qual o valor que o funcionário recebe por hora: "))
quantidade_horas_trabalhadas = int(input("Quantas horas o funcionário trabalhou no mês: "))

total_salario_mensal = valor_salario_por_hora * quantidade_horas_trabalhadas

print(f"O salário do funcionário que recebe R$ {valor_salario_por_hora:.2f} por hora trabalhada, "
      f"e trabalhou {quantidade_horas_trabalhadas} horas neste mês é de R$ {total_salario_mensal:.2f}")