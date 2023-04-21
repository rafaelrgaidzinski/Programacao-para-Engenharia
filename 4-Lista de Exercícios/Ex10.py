#   8) Desenvolva um programa que leia uma frase e um caractere. Em seguida,
#   exiba ambos e o número de ocorrências do caractere na frase.

print("Programa para contar quantas vezes um caractere aparece em uma frase")

frase = input("Informe uma frase: ")
caractere = input("Informe um caractere: ")

quantidade_caractere = frase.count(caractere)

print("Frase: " + frase, "Caractere: " + caractere, "Número de ocorrências do caractere na frase: " + str(quantidade_caractere), sep="\n")