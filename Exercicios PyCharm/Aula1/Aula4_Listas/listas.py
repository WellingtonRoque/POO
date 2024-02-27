"""
#Criando Listas em Python

# Lista vazia
lista_vazia = []

# Lista de números
numeros = [1, 2, 3, 4, 5]


# Lista de nomes
nomes = ["Alice", "Bob", "Charlie"]

# Lista mista
misturado = [1, "dois", 3.0, True]

print(lista_vazia)
print(numeros)
print(nomes)
print(misturado)

numeros = [1, 2, 3, 4, 5]
#Acessando Elementos em uma Lista
primeiro_elemento = numeros[0]
ultimo_elemento = numeros[4]
fatia = numeros[0:2]  # Elementos do índice 1 ao 3 (não inclusivo)

print(primeiro_elemento)
print(ultimo_elemento)
print(fatia)

#Modificando Listas em Python
numeros.append(6)          # Adiciona 6 ao final da lista
numeros[2] = "novo_valor"  # Modifica o valor no índice 1
del numeros[0]             # Remove o elemento no índice 2

print(numeros)



#Operações Comuns com Listas

numeros = [2, 3, 3, 4, 1]
# Operações com listas
tamanho = len(numeros)
soma = sum(numeros)
numeros.sort()          # Ordena a lista
quantidade_dois = numeros.count(3)

print(tamanho)
print(soma)
print(numeros)
print(quantidade_dois)

"""

# Criando uma lista de números pares de 0 a 10
numeros_pares = [x for x in range(0, 11, 2)]
print(numeros_pares)