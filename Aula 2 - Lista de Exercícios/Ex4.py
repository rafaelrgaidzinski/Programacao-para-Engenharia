#   4) Calcular a média aritmética simples de um aluno e mostrar a situação, que pode ser
#   aprovado ou reprovado! Critério de aprovação: média igual ou superior a 6

#   Descrição Narrativa
#   Receber o valor da primeira nota
#   Receber o valor da segunda nota
#   Obter a média aritmética somando as duas notas e dividindo por dois
#   Se a media for igual ou maior que 6 exibir aprovado senão exibir reprovado

#   Pseudocódigo
#   Algoritmo Media Aritmetica
#   var
#   media, primeiraNota, segundaNota: real
#   Inicio
#   escreva("Informe a primeira nota do aluno: ")
#   leia(primeiraNota)
#   escreva("Informe a segunda nota do aluno: ")
#   leia("segundaNota")
#   media <- (primeiraNota + segundaNota) / 2
#   se media >= 6
#   escreva("Aprovado")
#   senao
#   escreva("Reprovado")
#   fimSe
#   FimAlgoritmo

print("Programa para calcular a média de um aluno")

nota_1 = float(input("Informe a primeira nota:"))
nota_2 = float(input("Informe a segunda nota: "))

media = (nota_1 + nota_2) / 2

print("Média do aluno: ", media)

if (media >= 6):
    print("Situação do aluno: Aprovado")
else:
    print("Situação do aluno: Reprovado")



