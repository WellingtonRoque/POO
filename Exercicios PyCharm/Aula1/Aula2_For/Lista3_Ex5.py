"""
5 - Escreva um programa que apresenta os números divisores de um número
"""

num = int(input("Digite um numero: "))

for i in range(1,num+1):
    if num%i==0:
        print(i)