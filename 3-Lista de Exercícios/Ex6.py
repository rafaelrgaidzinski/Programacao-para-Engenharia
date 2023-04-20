#   4) Você está no Brasil, e para temperatura usamos o grau Celsius. Porém, quando você
#   for contratado para trabalhar como programador Python no exterior, deverá usar graus Fahrenheit.
#   Ou seja, você fornece a temperatura em graus Celsius, e seu script faz a conversão para graus Fahrenheit.

print("Programa para converter graus Celsius em Fahrenheit")

temp_celsius = float(input("Informe a temperatura em graus Celsius: "))

temp_fahrenheit = (temp_celsius * (9 / 5)) + 32
temp_fahrenheit = round(temp_fahrenheit, 2)

print("Temperatura em graus Celsius: " + str(temp_celsius), 
      "Temperatura em Fahrenheit: " + str(temp_fahrenheit), sep="\n")

