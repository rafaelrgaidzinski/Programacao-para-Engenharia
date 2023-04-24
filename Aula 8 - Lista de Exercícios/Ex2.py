#   2) Elabore um programa que leia um número inteiro e indique se o número é primo
#   ou não. Lembrando que os números primos são divisíveis somente por 1 e por ele
#   mesmo. No entanto, o número 1 não é primo.

print("Programa para verificar se um número é primo")

numero = int(input("Informe um número para verificar se é primo: "))

divisor = 1
contador = 0

while (divisor <= numero):
    if (numero % divisor == 0):
        contador += 1
    divisor += 1

if (contador <= 2):
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo!")