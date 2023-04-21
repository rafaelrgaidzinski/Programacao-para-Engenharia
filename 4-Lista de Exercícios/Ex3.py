#   3) Elaborar um programa que solicite nome e sobrenome. Em seguida, concatene ambos em uma nova string, separando com
#   espaço para que não fique como no exemplo apresentado anteriormente. Ao final, imprima o nome completo fornecido pelo usuário.

nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")

nome_completo = nome + " " + sobrenome

print("Nome completo: ", nome_completo)