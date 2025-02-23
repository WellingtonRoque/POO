"""
📌 Exercício 2. Controle de estoque
Crie um sistema para controlar o estoque de produtos.
O programa deve pedir a quantidade inicial de um produto, a quantidade vendida
e a quantidade recebida. Calcule a quantidade final em estoque.*
"""

# Solicita os dados ao usuário
qtd_inicial = int(input("Digite a quantidade inicial em estoque: "))
qtd_vendida = int(input("Digite a quantidade vendida: "))
qtd_recebida = int(input("Digite a quantidade recebida: "))

# Calcula a quantidade final em estoque
qtd_final = qtd_inicial - qtd_vendida + qtd_recebida

# Exibe o resultado
print(f"A quantidade final em estoque é: {qtd_final}")
