"""
Faça um programa para calcular o peso ideal, a partir da fórmula IMC = peso / altura2.
Nesse caso, solicite o peso e a altura do usuário, faça o cálculo e apresente a faixa de risco
correspondente, de acordo com a tabela seguinte:

"""

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso/altura**2

print("IMC: ",imc)

if imc<20:
    print("Abaixo do peso")
elif imc<=25:
    print("Normal")
elif imc<=30:
    print("Exceso de Peso")
elif imc<=35:
    print("Obesidade")
else:
    print("Obesidade Morbida")
