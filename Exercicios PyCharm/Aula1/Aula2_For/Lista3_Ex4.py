"""
4 - Escreva um programa que apresenta o Fatorial de um número.
Ex: Fat de 5 = 5X4X3X2X1 = 120.
"""
fatorial=1

fat = int(input("Digite o numero: "))

for i in range(1,fat+1):
    print(i)
    fatorial = fatorial*i

print("Fatorial = ",fatorial)