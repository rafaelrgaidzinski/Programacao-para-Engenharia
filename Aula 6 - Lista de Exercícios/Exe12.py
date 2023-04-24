# 12) Fazer um programa que solicita um número decimal e imprime o correspondente em hexa, binário e octal.

print("Programa para converter um decimal para hexadecimal, octal e binário")

numero_decimal = int(input("Informe um número inteiro para converter: "))

converter_numero_hexadecimal = numero_decimal
converter_numero_octal = numero_decimal
converter_numero_binario = numero_decimal

hexadecimal = ""
octal = ""
binario = ""

while (converter_numero_hexadecimal > 0):
    match (converter_numero_hexadecimal % 16):
        case 10:
            hexadecimal += "a"
        case 11:
            hexadecimal += "b"
        case 12:
            hexadecimal += "c"
        case 13:
            hexadecimal += "d"
        case 14:
            hexadecimal += "e"
        case 15:
            hexadecimal += "f"
        case _:
            hexadecimal += str(converter_numero_hexadecimal % 16)
    
    converter_numero_hexadecimal = converter_numero_hexadecimal // 16

print(f"Hexadecimal = {hexadecimal[::-1]}")


while (converter_numero_octal > 0):
    octal += str(converter_numero_octal % 8)
    converter_numero_octal = converter_numero_octal // 8

print(f"Octal = {octal[::-1]}")


while (converter_numero_binario > 0):
    binario += str(converter_numero_binario % 2)
    converter_numero_binario = converter_numero_binario // 2

print(f"Binário = {binario[::-1]}")




