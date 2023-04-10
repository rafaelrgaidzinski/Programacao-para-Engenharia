# 15) João Pescador, homem de bem, comprou um microcomputador para controlar o
#     rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
#     estabelecido pelo regulamento de pesca do Estado (50 quilos) deve pagar uma multa de
#     R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável
#     peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de
#     quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
#     os dados do programa com as mensagens adequadas.

print("Programa para calcular a multa do excesso de peso da pescaria")

quilos_pescados = float(input("Informe a quantidade de quilos de peixes que foram pescados: "))

if (quilos_pescados > 50):
    quilo_excedente = quilos_pescados - 50
    valor_multa = quilo_excedente * 4
    print(f"A pescaria excedeu em {quilo_excedente:.2f} kg o permitido por lei, com isso será necessário pagar a multa no valor de R$ {valor_multa:.2f}.")
else:
    print(f"A pescaria rendeu {quilos_pescados:.2f} kg e está dentro do permitido por lei.")