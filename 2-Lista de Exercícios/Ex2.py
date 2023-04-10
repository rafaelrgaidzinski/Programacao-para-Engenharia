#   2) Multiplicação de duas variáveis, para calcular a área do retângulo

#   Descrição Narrativa
#   1- Receber o valor das medidas da base e altura do retângulo
#   2- Realizar a multiplicação da base pela altura
#   3- Exibir o resultado da multiplicação

#   Pseudocódigo
#   Algoritmo Multiplicação
#   var
#   area, base, altura: inteiro
#   Inicio
#   escreva("Informe a medida da base do retângulo: ")
#   leia (base)
#   escreva("Informe a medida da altura do retângulo: ")
#   leia (altura)
#   area <- base * altura
#   escreva ("A área do retângulo é: ", area)
#   FimAlgoritmo

print("Programa para calcular a área de um retângulo")

base = int(input("Informe a medida da base do retângulo: "))
altura = int(input("Informe a medida da altura do retângulo: "))

area = base * altura

print("A área do retângulo é: ", area)