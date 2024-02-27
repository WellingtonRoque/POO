"""
4) Desenvolva um programa que solicite dois números inteiros, mostre a soma destes
números, e avise se a soma é maior, menor ou igual a 1000.

"""

num1 = int(input("Digite o numero 1: "))
num2 = int(input("Digite o numero 2: "))

soma = num1+num2

if soma > 1000:
    print("Soma = ", soma, "é maior que 1000")
else:
    if soma < 1000:
        print("Soma = ", soma, "é menor que 1000")
    else:
        print("Soma = ", soma, "é igual a 1000")

