"""
1 - Faça um programa que receba valores, mostrando na tela, e calcula a soma
e a média desses números.
Obs: O programa encerra quando receber um número negativo
"""
cont=0
valor=1
soma=0

while valor>=0:
    valor = float(input("Digite um valor: "))

    if valor>=0:
        cont+=1
        soma=soma+valor

print("Soma = ",soma)
print("Media = ",soma/cont)