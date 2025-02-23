"""
📌 Exercício 6. Simulação de descontos em uma compra
Crie um programa que simule um desconto progressivo em uma compra. O cliente recebe:
10% de desconto se o valor da compra for até R$ 500.
15% de desconto se o valor da compra for entre R$ 501 e R$ 1000.
20% de desconto se o valor da compra for acima de R$ 1000.
O programa deve pedir o valor total da compra e aplicar o desconto correspondente.
"""

valor = float(input("Digite o valor da compra: "))
if valor<=500:
    valor = valor*0.9
else:
    if valor<=1000:
        valor = valor*0.85
    else:
        valor = valor*0.8
print(f"Valor com desconto = {valor:.2f}")