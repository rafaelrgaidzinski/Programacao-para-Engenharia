#   7) Sua tarefa é criar um programa em Python que pede o preço original de um produto e
#   dá 20% de desconto. Você deve mostrar:
#   Preço original do produto
#   Valor do desconto em R$ (tipo 'Você ganhou R$ xx,xx de desconto’)
#   Valor do produto com o desconto

print("Programa para calcular o desconto de um produto")

preco_original = float(input("Informe o preço original do produto: "))

valor_desconto = preco_original * (20 / 100)
valor_desconto = round(valor_desconto, 2)

preco_com_desconto = preco_original - valor_desconto

print("Preço do produto: R$" + str(preco_original), "Você ganhou R$" + str(valor_desconto) + " de desconto",
      "Preço do produto com desconto: R$" + str(preco_com_desconto), sep="\n")