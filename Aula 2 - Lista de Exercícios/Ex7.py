#   3) Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem
#   um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75
#   centavos para cada exemplar adicional. Qual é o custo total de atacado para X
#   cópias? Solicite o valor de X.

print("Programa para calcular o preço de livros no atacado")

quantidade_livros = int(input("Informe a quantidade de livros que deseja comprar: "))

desconto = 1 - (40 / 100)
preco_livro = 24.95 * desconto

if (quantidade_livros > 0):
    custo_total = (quantidade_livros * preco_livro) + 3 + ((quantidade_livros - 1) * 0.75)
else:
    custo_total = 0

print("O custo total dos livros adquiridos é R$", round(custo_total, 2))

