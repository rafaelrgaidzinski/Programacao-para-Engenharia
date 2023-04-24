#   3) Mostrar o resultado da divisão de dois números

#   Descrição Narrativa
#   1- Receber o valor do dividendo (número que será dividido)
#   2- Receber o valor do divisor, que deve ser maior que zero
#   3- Dividir o dividendo pelo divisor
#   4- Exibir o resultado da divisão

#   Pseudocódigo
#   Algoritmo Divisão
#   var
#   divisao, dividendo, divisor: inteiro
#   Inicio
#   escreva("Informe o número que será o dividendo: ")
#   leia (dividendo)
#   escreva("Informe o número que será o divisor, sendo que o divisor deve ser maios que zero: ")
#   leia (divisor)
#   divisao <- dividendo / divisor
#   escreva("O resultado da divisão é: ", divisao)
#   FimAlgoritmo

print("Programa para realizar uma divisão")

dividendo = int(input("Informe o número que será o dividendo: "))
divisor = int(input("Informe o número que será o divisor, sendo que o divisor deve ser maior que zero: "))

divisao = int(dividendo / divisor)

print("O resultado da divisão é: ", divisao)