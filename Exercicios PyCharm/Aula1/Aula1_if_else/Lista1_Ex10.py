"""
10) Imagine uma prova com 100 questões, em que cada uma delas vale 1 ponto.
Nesse caso, faça um programa para divulgar o resultado a partir de conceitos,
de acordo com a seguinte tabela:
"""
resultado = int(input("Digite a quantidade de acertos: "))

if resultado<=50:
    print("Conceito D")
elif resultado<=70:
    print("Conceito C")
elif resultado<=90:
    print("Conceito B")
else:
    print("Conceito A")