""""
12) Faça um programa para ler três números e informar se eles podem ou não ser lados
de um triângulo. Caso os lados formem um triângulo, indique se o mesmo é: equilátero,
isósceles ou escaleno. Observação: Um triângulo é equilátero quando possui os três lados
iguais, isósceles quando possui dois lados iguais e escaleno quando não possui nenhum
dos lados iguais.
"""
lado1 = float(input("Digite o valor do lado 1: "))
lado2 = float(input("Digite o valor do lado 2: "))
lado3 = float(input("Digite o valor do lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Triangulo")
    if lado1 == lado2 == lado3:
        print("Equilatero")
    else:
        if lado1==lado2 or lado2 == lado3 or lado1==lado3:
            print("Isosceles")
        else:
            print("Escaleno")
else:
    print("Valores fora do padrao")