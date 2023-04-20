#   8) A loja percebeu que não quer dar 20% em tudo. Quer dar 20% em algumas coisas,
#   10% em outras, nada em outros produtos e até 30% em alguns outros produtos. Crie um
#   script em Python que pergunte o preço original e o desconto que deve ser concedido.
#   Ele deve mostrar a saída igual a do exercício anterior.

print("Programa para calcular descontos em produtos")

preco_original = float(input("Informe o preço original do produto: "))

opcao_desconto = 0
porcentagem_desconto = 0

while ((opcao_desconto < 1) or (opcao_desconto > 4)):
    print("Opções de desconto: \n 1- Não tem desconto" + 
            "\n 2- 10% de dewsconto \n 3- 20% de desconto \n 4- 30% de desconto")
    opcao_desconto = int(input("Informe a opção de desconto: "))
    
if (opcao_desconto == 1):
    porcentagem_desconto = 0
elif (opcao_desconto == 2):
    porcentagem_desconto = 10
elif (opcao_desconto == 3):
    porcentagem_desconto = 20
else:
    porcentagem_desconto = 30

valor_desconto = preco_original * (porcentagem_desconto / 100)
valor_desconto = round(valor_desconto, 2)

preco_com_desconto = preco_original - valor_desconto

print("Preço do produto: R$" + str(preco_original), "Você ganhou R$" + str(valor_desconto) + " de desconto",
      "Preço do produto com desconto: R$" + str(preco_com_desconto), sep="\n")