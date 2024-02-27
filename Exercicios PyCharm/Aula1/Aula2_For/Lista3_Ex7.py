""""
7 - Faça um programa que receba a idade e o peso de 7 pessoas, calcule e
mostre:
• A quantidade de pessoas com mais de 90 quilos;
• A média das idades das 7 pessoas.
• A quantidade de pessoas maiores de idade e abaixo de 60 quilos.
• A porcentagem de pessoas com idade entre 10 e 30 anos.
"""
cont_peso=0
cont_media=0
cont_idade=0
soma=0

for i in range(1,7):
    idade = float(input("Digite a idade: "))
    peso = float(input("Digite seu peso: "))

    soma = soma+idade;

    if peso>90:
        cont_peso+=1

    if idade>=18 and peso<60:
        cont_media+=1

    if(idade>10 and idade<30):
        cont_idade+=1
        print("")

print(" quantidade de pessoas com mais de 90 quilos: ", cont_peso)
print("A média das idades das 7 pessoas: ", soma/7)
print("A quantidade de pessoas maiores de idade e abaixo de 60 quilos: ",cont_media)
print("A porcentagem de pessoas com idade entre 10 e 30 ano: ", cont_idade/6*100)

