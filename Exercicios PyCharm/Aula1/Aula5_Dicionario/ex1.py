"""
Controle de Estoque:
Crie um sistema simples de controle de estoque,
onde o usuário pode adicionar produtos,
atualizar quantidades e verificar o estoque disponível.
"""

estoque = {

}
opcao = " "

while opcao != "sair":
    opcao = input(
        "Digite '1' para adicionar um produto, '2' para atualizar quantidade, '3' para verificar estoque, ou 'sair' para encerrar: ")

    if opcao == "sair":
        break
    elif  opcao == '1':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade inicial: "))

        estoque[produto] = quantidade
        print(f"Produto '{produto}' adicionado com estoque inicial de {quantidade} unidades.")

    elif opcao == '2':
        produto = input("Digite o nome do produto para atualizar a quantidade: ")

        if produto in estoque:
            quantidade_atualizada = int(input("Digite a quantidade atualizada: "))
            estoque[produto] = quantidade_atualizada
            print(f"A quantidade de '{produto}' foi atualizada para {quantidade_atualizada} unidades.")
        else:
            print(f"Produto '{produto}' não encontrado no estoque.")

    elif opcao == '3':
        print("\nEstoque Atual:")

        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade} unidades")

    else:
        print("Opção inválida. Por favor, escolha '1', '2', '3' ou 'sair'.")

# Exibe o estoque ao encerrar o programa
print("\nEstoque Final:")
for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade} unidades")