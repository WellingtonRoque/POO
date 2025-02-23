"""
📌 Exercício 3. Cálculo de pontuação de jogo
Crie um programa que calcule a pontuação total de um jogador em um jogo.
A pontuação será dada por:
10 pontos por cada vitória.
5 pontos por cada empate.
0 pontos por cada derrota.
"""

# Solicita o número de vitórias, empates e derrotas ao jogador
vitorias = int(input("Digite o número de vitórias: "))
empates = int(input("Digite o número de empates: "))
derrotas = int(input("Digite o número de derrotas: "))

# Calcula a pontuação total
pontuacao_total = (vitorias * 10) + (empates * 5) + (derrotas * 0)

# Exibe a pontuação total
print(f"A pontuação total do jogador é: {pontuacao_total}")
