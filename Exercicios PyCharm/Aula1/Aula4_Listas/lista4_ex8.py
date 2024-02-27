"""
8.	Dada uma lista de números,
substitua todos os valores pares por zero
"""
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista_numeros:
    if lista_numeros[i]%2==0:
        lista_numeros[i]=0
print(lista_numeros)