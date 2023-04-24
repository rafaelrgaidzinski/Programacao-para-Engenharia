#   3) Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa que auxilie os seus
#   eletricistas no cálculo das principais grandezas da eletricidade que são: Tensão, Resistência e Corrente. Sabe-se que U=Ri, onde,
#   U é a Tensão (em V), R é a Resistência (em Ώ) e i a Corrente (em A). Você foi contratado(a) pela empresa para atender a essa
#   solicitação. Construa um programa que apresente o seguinte menu:

#   ************************************************
#   CÁLCULO DE GRANDEZAS ELÉTRICAS
#   ************************************************
#   1. Tensão (em Volt)
#   2. Resistência (em Ohm)
#   3. Corrente (em Ampére)
#   ************************************************
#   Qual grandeza deseja calcular?

#   Em seguida, o programa deve solicitar que o eletricista informe o valor das outras duas grandezas para realizar o cálculo. Quando o
#   eletricista escolher:
#   a. Tensão, o programa deve solicitar que ele informe os valores da Resistência e da Corrente
#   b. Resistência, o programa deve solicitar que ele informe os valores da Tensão e da Corrente
#   c. Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência
#   Por fim, o programa deve calcular e apresentar o valor encontrado para a grandeza escolhida.


print("Programa para calcular grandezas elétricas")

opcao = 1
tensao = 0
resistencia = 0
corrente = 0

while (opcao != 4):
    print(60 * "*", 15 * " " + "CÁLCULO DE GRANDEZAS ELÉTRICAS", 60 * "*", "1. Tensão (em Volt)",
            "2. Resistência (em Ohm)", "3. Corrente (em Ampére)", "4. Sair", 60 * "*", sep="\n")
    
    opcao = int(input("Qual grandeza deseja calcular? "))

    match opcao:
        case 1:
            resistencia = float(input("Informe o valor da resistência em Ohms: "))
            corrente = float(input("Informe o valor da corrente em Ampéres: "))
            tensao = resistencia * corrente
            print(f"Tensão em Volts: {tensao:.2f}V")
        case 2:
            corrente = float(input("Informe o valor da corrente em Ampéres: "))
            tensao = float(input("Informe o valor da tensão em Volts: "))
            if (corrente > 0):
                resistencia = tensao / corrente
                print(f"Resistência em Ohms: {resistencia:.2f}Ω")
            else:
                print("Não foi possível realizar a divisão, pois o valor da corrente tem que ser diferente ZERO")
        case 3:
            resistencia = float(input("Informe o valor da resistência em Ohms: "))
            tensao = float(input("Informe o valor da tensão em Volts: "))
            if (resistencia > 0):
                corrente = tensao / resistencia
                print(f"Corrente em Ampéres: {corrente:.2f}A")
            else:
                print("Não foi possível realizar a divisão, pois o valor da resistência tem que ser diferente ZERO")
        case 4:
            print("Saindo...")
        case _:
            print("Opção inválida")
