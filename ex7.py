"""
📌 Exercício 7 - Tabuada
Peça para o usuário digitar um número e exiba a tabuada dele de 1 a 10.
"""
tab = int(input("Digite a tabuada: "))

for i in range(0, 11):
    print(f"{tab} * {i} = {tab*i}")