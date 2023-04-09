# 9) Desenvolva um programa que leia dois valores numéricos inteiros para duas variáveis e que
#    troque o conteúdo dessas variáveis, visualizando o valor das mesmas antes e depois da troca

print("Programa paratrocar o valor de duas variáveis")

variavel_1 = int(input("Informe o primeiro valor: "))
variavel_2 = int(input("Informe o segundo valor: "))

print(f'Valor da primeira variável: {variavel_1} \n'
      f'Valor da segunda variável: {variavel_2}')

variavel_de_transicao = variavel_1
variavel_1 = variavel_2
variavel_2 = variavel_de_transicao

print(f'Valor da primeira variável: {variavel_1} \n'
      f'Valor da segunda variável: {variavel_2}')