"""
Programa que solicita ao usuário inserir nomes e notas de alunos,
armazena essas informações em um dicionário e calcula a média das notas
"""
alunos_notas = {
}
nome = ""

while nome != "sair":
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome=="sair":
        break
    nota = float(input("Digite a nota do aluno: "))

    alunos_notas[nome] = nota

print(alunos_notas.values())

notas = list(alunos_notas.values())
print(len(notas))
media = sum(notas) / len(notas)

# Exibe as notas e a média
print("\nNotas dos alunos:")
for aluno, nota in alunos_notas.items():
    print(f"{aluno}: {nota}")

print(f"\nMédia das notas: {media:.2f}")