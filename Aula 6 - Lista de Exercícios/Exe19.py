#   19) Crie um Programa que leia três números e mostre o maior e o menor deles.

print("Programa para verificar o maior e o menor número")

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))
numero_3 = int(input("Informe o terceiro número: "))

maior = numero_1
menor = numero_1

if (numero_2 > maior):
    maior = numero_2

if (numero_3 > maior):
    maior = numero_3

if (numero_2 < menor):
    menor = numero_2

if (numero_3 < menor):
    menor = numero_3

print("O maior número é: ", maior)
print("O menor número é: ", menor)
