# Dada uma lista de números
lista_numeros_duplicatas = [1, 2, 3, 2, 4, 5, 3, 6]

# Remova os duplicados convertendo a lista para um conjunto e depois de volta para uma lista
lista_sem_duplicatas = list(set(lista_numeros_duplicatas))

# Imprima a lista sem duplicatas
print(lista_sem_duplicatas)