#   2) Faça um programa que calcule o fatorial de um número inteiro
#   fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120.

print("Calculadora de fatorial")

numero = int(input("Informe um número para calcular o fatorial: "))

fatorial = 1
mensagem = ""

for num in range(numero, 0, -1):
    fatorial *= num
    if (num == 1):
        mensagem += " " + str(num)
    else:
        mensagem += " " + str(num) + " ."


print(f"Fatorial de {numero}:", f"{numero}! = {mensagem} = {fatorial}", sep="\n")