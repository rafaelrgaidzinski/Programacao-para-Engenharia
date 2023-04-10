#   18) Elabore um Programa que leia três números e mostre o maior deles.

print("Programa para verificar qual o maio rnúmero")

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))
numero_3 = int(input("Informe o terceiro número: "))

maior = numero_1

if (numero_2 > maior):
    maior = numero_2

if (numero_3 > maior):
    maior = numero_3

print("O maior número é: ", maior)
