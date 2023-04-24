#   3) Para construir o programa a seguir, considere que os usuários só informarão
#   números inteiros positivos. Crie um programa que receba 5 números digitados e, ao
#   final, exiba a quantidade de números pares.

print("Programa para verificar a quantidade de números pares")

quantidade_numeros = 0
quantidade_numeros_pares = 0

while (quantidade_numeros < 5):
    numero = int(input("Informe um número positivo: "))
    while (numero < 0):
        numero = int(input("Informe um número positivo: "))
    if (numero % 2 == 0):
        quantidade_numeros_pares += 1
    quantidade_numeros += 1

print("Quantidade de números pares:", quantidade_numeros_pares)
