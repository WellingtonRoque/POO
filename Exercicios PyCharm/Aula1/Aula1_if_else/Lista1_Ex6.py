"""
6) Escreva um programa para ler as três notas obtidas por um aluno durante
o semestre.
Calcular a sua média (aritmética) e informar a sua menção Aprovado (media
>= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 e 6.9).
"""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1+nota2+nota3)/3

if media>=7:
    print("Aprovado")
else:
    if media>5:
        print("Recuperação")
    else:
        print("Reprovado")