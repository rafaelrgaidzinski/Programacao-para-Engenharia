#   6) Um novo modelo de carro, super econômico foi lançado. Ele faz 20 km com 1 litro de
#   combustível. Cada litro de combustível custa R$ 4,95.
#   Faça um programa que pergunte ao usuário quanto de dinheiro ele pretende usar e em
#   seguida o programa informa quantos litros de combustível ele pode comprar e quantos
#   quilômetros o carro consegue rodar com esta quantidade de combustível.
#   Seu script será usado no computador de bordo do carro.

print("Programa para calcular quantos litros de combustível o motorista consegue comprar")

PRECO_COMBUSTIVEL = 4.95
KM_POR_LITRO = 20

dinheiro_disponivel = float(input("Informe quanto dinheiro tem disponível para comprar combustível: "))

litros_combustivel = dinheiro_disponivel / PRECO_COMBUSTIVEL
litros_combustivel = round(litros_combustivel, 2)

quantidade_kms = litros_combustivel * KM_POR_LITRO
quantidade_kms = round(quantidade_kms, 2)

print("Quantidade de litros: " + str(litros_combustivel) + " litros",
      "Autonomia: " + str(quantidade_kms) + " kms", sep="\n")



