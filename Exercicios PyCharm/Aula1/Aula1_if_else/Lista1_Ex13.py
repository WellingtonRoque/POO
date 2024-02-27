"""
13) Faça um programa que determine se um ano é bissexto. Observação: São bissextos
todos os anos divisíveis por 4, excluindo os que sejam divisíveis por 100, porém, não os
que sejam divisíveis por 400.
"""
ano = float(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano Bissesto")
else:
    print("Ano Normal")