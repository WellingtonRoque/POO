"""
📌 Exercício 9 - Somando Números Pares
Some todos os números pares de 1 a 100 e exiba o resultado.
"""
soma = 0

for i in range(0, 101, 2):
    print(i)
    soma = soma + i
print(f"Soma dos pares: {soma}")