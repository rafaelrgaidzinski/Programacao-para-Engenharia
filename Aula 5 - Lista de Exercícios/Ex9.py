#   5) Um posto de abastecimento está comercializando combustíveis com a seguinte tabela de descontos:

#   Álcool: até 20 litros, desconto de 2% por litro;
#   acima de 20 litros, desconto de 5% por litro;

#   Gasolina: até 20 litros, desconto de 4% por litro;
#   acima de 20 litros, desconto de 6% por litro;

#   Desenvolva um programa em Python que leia o número de litros vendidos e o tipo de
#   combustível (codificado com A – Álcool e G – Gasolina), calcule e imprima o valor a ser
#   pago pelo cliente, sabendo que o litro da gasolina está em R$ 5,57 e do álcool R$ 4,98.

print("Programa para calcular o valor a ser pago no abastecimento")

quantidade_litros = float(input("Informe quantos litros de combustível foram abastecidos: "))

tipo_combustivel = input("Qual o tipo de combustível foi abastecido: \n A - Álcool \n G - Gasolina \n").lower()

PRECO_GASOLINA = 5.57
PRECO_ALCOOL = 4.98
total_gasto = 0

if (tipo_combustivel == "a"):
    if (quantidade_litros > 20):
        total_gasto = quantidade_litros * (PRECO_ALCOOL - (PRECO_ALCOOL * (5/100))) 
    else:
        total_gasto = quantidade_litros * (PRECO_ALCOOL - (PRECO_ALCOOL * (2/100))) 
elif (tipo_combustivel == "g"):
    if (quantidade_litros > 20):
        total_gasto = quantidade_litros * (PRECO_GASOLINA - (PRECO_GASOLINA * (6/100))) 
    else:
        total_gasto = quantidade_litros * (PRECO_GASOLINA - (PRECO_GASOLINA * (4/100))) 
else:
    print("O tipo de combustível informado não está disponível")

if (total_gasto > 0):
    print(f"Foram abastecidos {quantidade_litros:.0f} litros de", "álcool" if tipo_combustivel == "a" else "gasolina", f"e o valor total a ser pago é de R${total_gasto:.2f}")
