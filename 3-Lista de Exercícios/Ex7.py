#   5) Agora faça o contrário. Você fornece a temperatura em graus Fahrenheit, seu
#   programa converte para Celsius e exibe na tela.

print("Programa para converter Fahrenheit em graus Celsius")

temp_fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

temp_celsius = (temp_fahrenheit - 32) * (5 / 9)
temp_celsius = round(temp_celsius, 2)

print("Temperatura em Fahrenheit: " + str(temp_fahrenheit),
      "Temperatura em graus Celsius: " + str(temp_celsius), sep="\n")