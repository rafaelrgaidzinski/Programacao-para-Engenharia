#   17) Faça um programa para a leitura de duas notas parciais de um aluno. O programa
#   deve calcular a média alcançada pelo aluno e apresentar:
#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menor do que sete;
#   A mensagem "Aprovado com Distinção", se a média for igual a dez.

print("Programa para calcular a média do aluno")

nota_1 = float(input("Informe a primeira nota do aluno: "))
nota_2 = float(input("Informe a segunda nota do aluno: "))

media = (nota_1 + nota_2) / 2

if (media == 10):
    print("Aprovado com Distinção")
elif (media >= 7):
    print("Aprovado")
else:
    print("Reprovado")