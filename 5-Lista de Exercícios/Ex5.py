#   1) Desenvolva um script que solicite dois números quaisquer e mostre o maior entre eles

print("Programa para identificar o maior entre dois números")

primeiro_numero = int(input("Informe o primeiro número: "))
segundo_numero = int(input("Informe o segundo número: "))

maior_numero = primeiro_numero

if (segundo_numero > primeiro_numero):
    maior_numero = segundo_numero

print("O maior número é ", maior_numero)


