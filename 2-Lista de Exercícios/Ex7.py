print("Programa para calcular o preço de livros no atacado")

quantidade_livros = int(input("Informe a quantidade de livros que deseja comprar: "))

desconto = 1 - (40 / 100)
preco_livro = 24.95 * desconto

if (quantidade_livros > 0):
    custo_total = (quantidade_livros * preco_livro) + 3 + ((quantidade_livros - 1) * 0.75)
else:
    custo_total = 0

print("O custo total dos livros adquiridos é R$", round(custo_total, 2))

