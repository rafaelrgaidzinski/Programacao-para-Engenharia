#   3) Uma imobiliária paga aos seus corretores um salário base de R$
#   1.500,00. Além disso, uma comissão de R$ 200,00 por cada imóvel
#   vendido e 5% do valor de cada venda. Construa um programa que
#   solicite o nome do corretor, a quantidade de imóveis vendidos e o valor
#   total de suas vendas. Ao fim, o programa deve calcular e escrever o
#   salário final do corretor de imóveis.

print("Programa para calcular o salário de um corretor com base na comissão")

nome_corretor = input("Informe o nome do corretor: ")
quantidade_imoveis_vendidos = int(input(f"Informe a quantidade de imóveis vendidos pelo corretor {nome_corretor}: "))
valor_total_imoveis_vendidos = float(input(f"Informe o valor total das vendas de imóveis pelo corretor {nome_corretor}: "))

SALARIO_BASE = 1500

salario_final = SALARIO_BASE + (quantidade_imoveis_vendidos * 200) + (valor_total_imoveis_vendidos * (5 / 100))

print(f"O corretor {nome_corretor} deverá receber com as comissões adicionadas ao salário o valor de R${salario_final: .2f}")
