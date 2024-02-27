"""
4.	Dada uma lista de palavras,
crie uma nova lista com o comprimento de cada palavra.
"""

palavras = ["python", "poo", "devops"]
print(palavras)

qtd = [len(palavra) for palavra in palavras]
print(qtd)
