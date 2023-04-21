#   3) Elabore um programa que solicite uma frase ao usuário e escreva a frase
#   toda em maiúscula. No mesmo programa exiba a frase sem espaços em branco.

print("Programa para converter letras minúsculas em maiúsculas e remover espaços em branco")

frase = input("Informe uma frase: ")

frase = frase.upper().replace(" ", "")

print("Frase com letras maiúsculas e sem espaço em branco: " + frase)