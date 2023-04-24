#   1) Desenvolva um script Python que lê vários números positivos via teclado. Quando o
#   número lido for negativo, o script deve parar e exibir a soma de todos os números positivos
#   inseridos, a média desses números, o menor e o maior número digitado.

print("Programa para realizar a soma de números positivos")

numero = int(input("Informe um número: "))

maior_numero = numero
menor_numero = numero
soma = numero
media = 0
contador = 1

while (numero >= 0):
    numero = int(input("Informe um número: "))
    if (numero >= 0):
        soma += numero
        if (numero > maior_numero):
            maior_numero = numero
        if (numero < menor_numero):
            menor_numero = numero
        contador += 1

media = soma / contador

print(f"Soma dos números positivos: {soma}", 
      f"Média dos números positivos: {media:.1f}",
      f"Maior número: {maior_numero}",
      f"Menor número: {menor_numero}", sep="\n")