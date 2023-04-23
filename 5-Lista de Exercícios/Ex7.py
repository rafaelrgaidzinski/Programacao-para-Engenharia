#   3) Elabore um programa que verifique se uma letra digitada é "F" ou "M". Conforme a
#   letra escrever: F - Feminino, M – Masculino ou Sexo Inválido.

print("Programa para verificar o sexo informado")

sexo = input("Informe o sexo: ")

if (sexo.upper() == "F"):
    print("Sexo: F - Feminino")
elif (sexo.upper() == "M"):
    print("Sexo: M - Masculino")
else:
    print("Sexo Inválido")

