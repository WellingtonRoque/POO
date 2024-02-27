"""
7) Desenvolva um programa para calcular e mostrar o desconto no valor de uma compra
(fornecido pelo usuário), de acordo com a tabela:
"""

valor = float(input("Digite o valor da compra: "))

if valor<1000:
    print("10% de Desconto = ",valor*0.9)
else:
    if valor<5000:
        print("20% de Desconto = ", valor * 0.8)
    else:
        print("30% de Desconto = ", valor * 0.7)
