"""
9) Elabore um programa, que solicite ao usuário a velocidade do veículo e apresente na
tela a penalidade, de acordo com a tabela a seguir:
"""
velocidade = float(input("Digite a valocidade: "))

if velocidade<=60:
    print("Sem Penalidade")
elif velocidade<=80:
    print("Multa Leve")
elif velocidade<=100:
    print("Multa Grave")
elif velocidade<=120:
    print("Multa Gravissima")
else:
    print("Detenção do Condutor")