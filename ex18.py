"""
📌 Exercício 18- Média de Notas
Crie uma função calcular_media(notas) que recebe uma lista de notas e retorna a média.
"""


def calcular_media(notas):
    if len(notas) == 0:
        return 0  # Se a lista de notas estiver vazia, retorna 0
    return sum(notas) / len(notas)


# Função para coletar as notas do usuário
def coletar_notas():
    notas = []
    while True:
        entrada = input("Digite uma nota (ou 'fim' para terminar): ")

        if entrada.lower() == 'fim':  # Se o usuário digitar 'fim', encerra a coleta
            break

        # Converte a entrada para float e adiciona à lista
        notas.append(float(entrada))

    return notas


# Coletando as notas
notas = coletar_notas()

# Calculando a média
media = calcular_media(notas)
print(f"A média das notas é: {media:.2f}")
