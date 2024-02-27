"""
6.	Dada uma lista de nomes,
verifique se um nome específico está presente nela
"""
# Dada uma lista de nomes
lista_nomes = ["Ana", "Carlos", "Beatriz", "Daniel", "Eduardo"]

# Nome a ser verificado
nome_verificar = "Eduardo"

# Verifica se o nome está presente na lista
if nome_verificar in lista_nomes:
    print(f"{nome_verificar} está presente na lista.")
else:
    print(f"{nome_verificar} não está presente na lista.")