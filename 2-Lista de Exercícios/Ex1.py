#   1) Obter a soma de 3 variáveis numéricas inteiras!

#   Descrição Narrativa
#   1- Receber o valor dos 3 números
#   2- Realizar a soma dos 3 números
#   3- Exibir o resultado da soma

#   Pseudocódigo
#   Algoritmo "Soma"
#   var
#   soma, num1, num2, num3: inteiro
#   Inicio
#   escreva ("Digite o valor do primeiro número: ")
#   leia (num1)
#   escreva("Digite o valor do segundo número: ")
#   leia (num2)
#   escreva("Digite o valor do terceiro número: ")
#   leia (num3)
#   soma <- num1 + num2 + num3
#   escreva ("A soma é igual a: ", soma)
#   FimAlgoritmo

print("Algoritmo Soma")

num_1 = int(input("Digite o valor do primeiro número: "))
num_2 = int(input("Digite o valor do segundo número: "))
num_3 = int(input("Digite o valor do terceiro número: "))

soma = num_1 + num_2 + num_3

print("A soma é igual a: ", soma)
