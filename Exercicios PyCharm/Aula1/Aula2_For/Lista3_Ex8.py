"""
8) Faça um programa que leia um número n e imprima se ele é primo ou não.
(um número primo tem apenas 2 divisores: 1 e ele mesmo! O número 1 não é
primo!!!)
"""
cont=0
num = int(input("Digite um numero: "))

for i in range(1, num):
    if num%i==0:
        cont+=1

print("cont = ",cont)

if cont==1:
    print("Numero Primo")
else:
    print("Numero")

