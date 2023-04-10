#   20) Desenvolva um Programa que peça os 3 lados de um triângulo. O programa deverá
#   informar se os valores podem formar um triângulo. Indique, caso os lados formem um
#   triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#   Dicas:
#   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   Triângulo Escaleno: três lados diferentes.

print("Programa para verificar se é um triângulo e qual o tipo")

lado_1 = int(input("Informe o primeiro lado do triângulo: "))
lado_2 = int(input("Informe o segundo lado do triângulo: "))
lado_3 = int(input("Informe o terceiro lado do triângulo: "))

if ((lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1)):
    if (lado_1 == lado_2 == lado_3):
        print("É um triângulo equilátero")
    elif ((lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3)):
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Esta forma geométrica não é um triângulo")