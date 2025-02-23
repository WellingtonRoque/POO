"""
📌 Exercício 11 - Números Primos
Desafio: Peça ao usuário para digitar um número e informe se ele é primo.
"""
cont = 0

num = int(input("Digite o Numero: "))

for i in range(num, 0, -1):
    print(i)
    if (num%i==0):
        cont+=1
        print(f"cont = {cont}")
if cont>2:
    print("não primo")
else:
    print("Primo")