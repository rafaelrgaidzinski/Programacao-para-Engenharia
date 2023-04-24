#   2) Crie um programa que peça um valor e imprima na tela se o valor é positivo,
#   negativo ou ainda igual a zero.

print("Programa para verificar se um número é positivo, negativo ou zero")

numero = int(input("Informe um número: "))

if (numero > 0):
    print(f"O número {numero} é positivo!")
elif (numero < 0):
    print(f"O número {numero} é negativo!")
else:
    print("O número é igual a zero!")