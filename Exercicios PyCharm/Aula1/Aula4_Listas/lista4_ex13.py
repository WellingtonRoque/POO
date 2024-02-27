# Dada uma lista de palavras
lista_palavras = ["Abacaxi", "Banana", "Amor", "Cachorro", "Alegria"]

# Crie uma nova lista apenas com palavras que começam com 'A'
lista_com_A = [palavra for palavra in lista_palavras if palavra.startswith('A')]

# Imprima a nova lista
print(lista_com_A)