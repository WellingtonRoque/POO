"""
📌 Exercício 12 - Adivinhação
O programa escolhe um número aleatório entre 1 e 10, e o usuário tem que adivinhar.
Ele só para quando o número correto for digitado.
"""
import random
cont=0

while True:

    # Gerar um número inteiro aleatório entre 1 e 10 (inclusive)
    aleatorio = random.randint(1, 10)
    print(aleatorio)

    num = int(input("Digite um numero: "))

    if num==aleatorio:
        print("VocÊ acertou")
        break
    else:
        print("Tente novamente")
        cont+=1
print(f"Quantidade de tentativas: {cont}")
