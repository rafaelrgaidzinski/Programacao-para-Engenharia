#   2) Elabore um programa que leia um número inteiro e indique se o número é primo
#   ou não. Lembrando que os números primos são divisíveis somente por 1 e por ele
#   mesmo. No entanto, o número 1 não é primo.
   
import math, time

print("Programa para verificar se um número é primo!")

numero = int(input("Informe um número para verificar se é primo: "))

contador = 0
divisor = 2

start = time.time()

raiz_numero = int(math.sqrt(numero) + 1)   

while (contador < 1 and divisor <= raiz_numero):
    if (numero <= 3):
        break
    if (numero % divisor == 0):
        contador += 1
    divisor += 1
    
end = time.time()

if (contador > 0 or numero == 1):
    print(f"O número {numero} não é primo!")
    print(f"Tempo de execução: {end - start: .2f} seg")
else:
    print(f"O número {numero} é primo!") 
    print(f"Tempo de execução: {end - start: .2f} seg")
