"""
📌 Exercício 5. Cálculo de salário líquido
Crie um programa que calcule o salário líquido de um funcionário.
O salário bruto é dado pelo usuário, e o programa deve descontar:
INSS (10%)
Imposto de Renda (IR) de acordo com a faixa salarial:
Até R$ 2.000,00: isento
De R$ 2.001,00 até R$ 5.000,00: 10%
Acima de R$ 5.000,00: 20%
"""

# Solicita o salário bruto ao usuário
salario_bruto = float(input("Digite o salário bruto do funcionário: R$ "))

# Desconto do INSS (10% do salário bruto)
inss = 0.10 * salario_bruto

# Cálculo do Imposto de Renda (IR) de acordo com a faixa salarial
if salario_bruto <= 2000:
    ir = 0  # isento de IR
elif salario_bruto <= 5000:
    ir = 0.10 * salario_bruto  # 10% de IR
else:
    ir = 0.20 * salario_bruto  # 20% de IR

# Cálculo do salário líquido
salario_liquido = salario_bruto - inss - ir

# Exibe o salário líquido
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (10%): R$ {inss:.2f}")
print(f"Desconto Imposto de Renda (IR): R$ {ir:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
