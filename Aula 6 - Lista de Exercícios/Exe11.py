# 11) Elabore um programa que determine se um ano introduzido pelo usuário é ou não
#     bissexto. Um ano é bissexto se for múltiplo de 4 sem ser de 100 ou se for múltiplo de 400.


print("Programa para verificar se um determinado ano é bissexto")

ano = int(input("Informe um ano para verificar se é bissexto ou não: "))

if ((ano % 4 == 0) and (ano % 100 != 0)):
    print(f'O ano {ano} é bissexto!')
elif (ano % 400 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')