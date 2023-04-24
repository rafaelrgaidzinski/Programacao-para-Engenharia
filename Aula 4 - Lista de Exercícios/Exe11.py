#   9) Elabore um programa que leia uma frase, uma palavra antiga e uma palavra
#   nova. O programa deve exibir uma string contendo a frase original e outra com
#   a ocorrência da palavra antiga substituída pela palavra nova.

print("Programa para substituir uma palavra antiga por uma nova")

frase = input("Informe uma frase: ")
palavra_antiga = input("Informe a palavra que deseja substituir na frase: ")
palavra_nova = input("Informe a palavra que irá substituir: ")

frase_nova = frase.replace(palavra_antiga, palavra_nova)

print("Frase antiga: " + frase, "Frase nova: " + frase_nova, sep="\n")