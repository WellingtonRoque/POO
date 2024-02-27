""""
14) Faça um programa que leia três números e mostre o maior e o menor deles.
"""

numero1 = int(input("Digite o numero 1: "))
numero2 = int(input("Digite o numero 2: "))
numero3 = int(input("Digite o numero 3: "))

# Encontrar o maior número
if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    maior = numero2
else:
    maior = numero3

print("Maior = ",maior)

# Encontrar o menor número
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
else:
    menor = numero3

print("Menor = ", menor)