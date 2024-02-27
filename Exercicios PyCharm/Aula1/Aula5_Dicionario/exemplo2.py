"""
Histórico de Compras:
Crie um programa que mantém o histórico de compras de um cliente,
armazenando itens comprados e suas quantidades em um dicionário.
"""
historico_compras = {

}
produto = " "

while produto != "sair":
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if produto == "sair":
        break
    quantidade = int(input("Digite a quantidade comprada: "))

    # Atualiza o histórico de compras
    if produto in historico_compras:
        historico_compras[produto] += quantidade
    else:
        historico_compras[produto] = quantidade

print(historico_compras.keys())
print(historico_compras.values())

# Exibe o histórico de compras
if historico_compras:
    print("\nHistórico de Compras:")
    for produto, quantidade in historico_compras.items():
        print(f"{produto}: {quantidade} unidades")
else:
    print("Nenhuma compra foi registrada.")