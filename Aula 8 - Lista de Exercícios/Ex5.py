#   1) Faça um programa que apresente um menu de opções para o cálculo das
#   seguintes operações entre dois números:
#   • adição (opção 1)
#   • subtração (opção 2)
#   • multiplicação (opção 3)
#   • divisão (opção 4)
#   • saída (opção 5)
#   O programa deve possibilitar ao usuário a escolha da operação desejada, a
#   exibição do resultado e a volta ao menu de opções. O programa somente termina
#   quando for escolhida a opção de saída (opção 5).

print("Calculadora")

opcao = 0
resultado = 0

while (opcao != 5):
    primeiro_numero = int(input("Informe o primeiro número da operação: "))
    segundo_numero = int(input("Informe o segundo número da operação: "))

    opcao = int(input("Qual operação deseja realizar: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Sair \n"))

    match opcao:
        case 1:
            resultado = primeiro_numero + segundo_numero
            print("Resultado da soma:", resultado)
        case 2:
            resultado = primeiro_numero - segundo_numero
            print("Resultado da subtração:", resultado)
        case 3:
            resultado = primeiro_numero * segundo_numero
            print("Resultado da multiplicação:", resultado)
        case 4:
            if (segundo_numero != 0):
                resultado = primeiro_numero / segundo_numero
                print("Resultado da divisão:", round(resultado, 2))
            else:
                print("Não é possível realizar uma divisão por ZERO")
        case 5:
            print("Saindo...")
        case _:
            print("Opção inválida")  
