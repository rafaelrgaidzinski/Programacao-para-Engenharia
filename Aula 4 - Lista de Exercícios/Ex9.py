#   7) Elabore um programa que leia o nome do usuário e mostre o nome de traz
#   para frente, utilizando somente letras maiúsculas.

print("Programa para inverter o nome e tornar todas as letras maiúsculas")

nome = input("Informe seu nome: ")

nome = nome.upper()[::-1]

print("Nome de trás para frente com letras maiúsculas: " + nome)