"""
📌 Exercício 17 - Verificar Número Par ou Ímpar
Crie uma função eh_par(numero) que recebe um número e
retorna True se for par e False se for ímpar.
"""
def eh_par(a):
    if a % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um valor: "))

if eh_par(num) == True:
    print(f"PAR: {num}")
else:
    print(f"IMPAR: {num}")