"""
8) Um posto de combustível vende três tipos de combustível: álcool, diesel e gasolina. O
preço de cada litro de combustível é apresentado na tabela a seguir. Faça um programa
que leia um caractere que representa o tipo de combustível comprado (a, d ou g) e a
quantidade em litros. O programa deve imprimir o valor em reais a ser pago pelo
combustível
"""
alcool = 4
diesel = 7
gasolina = 6

tipo = input("Qual combustivel deseja abastecer: ")
litros = float(input("Digite a quantidade de litros: "))

if tipo == 'a':
    print("Alcool = ", litros*alcool)
else:
    if tipo == 'd':
        print("Diesel = ", litros*diesel)
    else:
        if tipo == 'g':
            print("Gasolina = ",litros*gasolina)
        else:
            print("entrada invalida")