""""
11) Tendo como dados de entrada a altura e o sexo de uma pessoa, faça um programa que
calcule seu peso ideal, utilizando as seguintes fórmulas:
- para homens: (72.7 * h) - 58;
- para mulheres: (62.1 * h) - 44.7
"""
altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")

if sexo == 'm':
    print("Peso ideal: ", 72.7 * altura -58)
else:
    if sexo == 'f':
        print("Peso ideal: ",(62.1 * altura)-44.7)
    else:
        print("Entrada Invalida")
