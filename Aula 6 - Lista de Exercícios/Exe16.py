#   16) Desenvolva um Programa que pergunte quanto você ganha por hora e o número de
#   horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#   sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
#   para o sindicato, faça um programa que nos dê:
#   • salário bruto.
#   • quanto pagou ao INSS.
#   • quanto pagou ao sindicato.
#   • o salário líquido.
#   Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$

print("Programa para calcular o salário liquido mensal")

valor_hora_trabalhada = float(input("Informe o valor que o funcionário recebe por hora: "))
horas_trabalhadas = int(input("Informe quantas horas o funcionário trabalhou neste mês: "))

salario_bruto = valor_hora_trabalhada * horas_trabalhadas

desconto_IR = salario_bruto * (11 / 100)
desconto_INSS = salario_bruto * (8 / 100)
desconto_sindicato = salario_bruto * (5 / 100)

salario_liquido = salario_bruto - (desconto_IR + desconto_INSS + desconto_sindicato)

print("+ Salário Bruto : R$ ", salario_bruto)
print("- IR (11%) : R$ ", desconto_IR)
print("- INSS (8%) : R$ ", desconto_INSS)
print("- Sindicato (5%) : R$ ", desconto_sindicato)
print("= Salário Liquido : R$ ", salario_liquido)

