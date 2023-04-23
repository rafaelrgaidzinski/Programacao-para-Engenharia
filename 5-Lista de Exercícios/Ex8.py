#   4) Escreva um programa que verifique se uma letra digitada é vogal ou consoante. Ou
#   ainda se não está nestes grupos.

print("Programa para verificar se uma letra é vogal ou consoante")

letra = input("Informe uma letra: ").lower()

if (letra.isalpha()):
   match letra:
        case "a":
           print("A letra digitada é uma vogal!")
        case "e":
           print("A letra digitada é uma vogal!")
        case "i":
           print("A letra digitada é uma vogal!")
        case "o":
           print("A letra digitada é uma vogal!")
        case "u":
           print("A letra digitada é uma vogal!")
        case _:
            print("A letra digitada é uma consoante!")
else:
    print("O caractere informado não pertence ao alfabeto!")

