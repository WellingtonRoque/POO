"""
📌 Exercício 10 - Contando Vogais
Peça ao usuário para digitar uma palavra e conte quantas vogais existem nela.
"""
vogais = "AaEeIiOoUu"
cont_vogais=0

palavra = input("Digite uma palavra: ")

for letra in palavra:
    if letra in vogais:
        cont_vogais+=1
print(f"Qtd de Vogais: {cont_vogais}")
