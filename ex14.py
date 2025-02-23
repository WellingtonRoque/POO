"""
📌 Exercício 14 - Validando Entrada do Usuário
Peça para o usuário digitar um número positivo.
"""

while True:
    numero = float(input("Digite um número positivo: "))

    if numero >= 0:
        print(f"Você digitou o número {numero}, que é válido.")
        break
    else:
        print("Número inválido! Tente novamente.")
