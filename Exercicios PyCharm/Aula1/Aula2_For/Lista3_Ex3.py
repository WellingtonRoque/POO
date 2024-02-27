"""
3 - Escreva um programa em C que lê 15 valores reais, encontra o maior e o
menor deles e mostra o resultado.
"""
maior=0
menor=0

for i in range(1,6):



    #print(i)
    valor = int(input("Entre com o valor: "))

    if i==1:
        maior=valor
        menor=valor

    if valor>maior:
        maior=valor

    if valor<menor:
        menor=valor

print("Maior = ", maior)
print("Menor = ", menor)