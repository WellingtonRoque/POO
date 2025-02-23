"""
📌 Exercício 16 - Calculadora

Crie uma função calculadora(a, b, operacao) que recebe dois números e
uma operação (+, -, *, /) e retorna o resultado.
"""
def soma(a, b):
    return a+b
def sub(a, b):
    return a-b
def mult(a, b):
    return a*b
def div(a, b):
    return a/b

num1 = float(input("Digite o numero 1: "))
num2 = float(input("Digite o numero 2: "))

print(f"soma: {soma(num1,num2)}")
print(f"soma: {sub(num1,num2)}")
print(f"soma: {mult(num1,num2)}")
print(f"soma: {div(num1,num2)}")


