"""
📌 Exercício 4. Cálculo de comissão de vendedor
Crie um programa que calcule a comissão de um vendedor, com base nas vendas realizadas.
O vendedor ganha 5% de comissão sobre as vendas, mas existe um bônus de R$ 200,00
se ele vender mais de R$ 10.000,00 no mês.
Fórmula:
Comissão = 5% do valor das vendas
Se as vendas forem acima de R$ 10.000,00 adicionar o bônus de R$ 200.
"""
# Solicita o valor das vendas ao usuário
vendas = float(input("Digite o valor total das vendas do mês: R$ "))

# Calcula a comissão de 5% sobre o valor das vendas
comissao = 0.05 * vendas

# Verifica se as vendas ultrapassaram R$ 10.000,00 e aplica o bônus
if vendas > 10000:
    comissao += 200  # Bônus de R$ 200,00

# Exibe o valor da comissão
print(f"A comissão do vendedor é: R$ {comissao:.2f}")
