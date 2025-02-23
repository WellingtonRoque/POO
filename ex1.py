"""
📌Exercício 1. Parcelamento de um produto
Uma loja oferece parcelamento de um produto,
mas cobra 10% de juros ao parcelar.
Peça ao usuário o preço do produto e o número de parcelas e
calcule o valor total e o valor de cada parcela.
"""

preco = float(input("Digite o preço do produto: "))
parcela = float(input("Digite a quantidade de parcelas: "))
reajuste = preco * 1.1 / parcela
print(f"Valor total com reajuste de 10%: {preco * 1.1:.2f}")
print(f"Valor das parcelas: {reajuste:.2f}")