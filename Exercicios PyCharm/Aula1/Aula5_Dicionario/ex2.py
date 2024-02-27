"""
Agenda Telefônica:
Implemente uma agenda telefônica utilizando dicionários,
onde o usuário pode adicionar contatos,
buscar por número de telefone e remover contatos.
"""
agenda_telefonica = {

}
opcao = ""

while opcao != "sair":
    opcao = input("Digite '1' para adicionar um contato, '2' para buscar por número, '3' para remover um contato, ou 'sair' para encerrar: ")

    if opcao == "sair":
        break

    elif opcao == '1':
        nome = input("Digite o nome do contato: ")
        numero_telefone = input("Digite o número de telefone: ")

        agenda_telefonica[nome] = numero_telefone
        print(f"Contato '{nome}' adicionado com número '{numero_telefone}'.")

    elif opcao == '2':
        nome_busca = input("Digite o nome do contato para buscar o número: ")

        if nome_busca in agenda_telefonica:
            print(f"O número de telefone de '{nome_busca}' é '{agenda_telefonica[nome_busca]}'.")
        else:
            print(f"Contato '{nome_busca}' não encontrado na agenda.")

    elif opcao == '3':
        nome_remover = input("Digite o nome do contato para remover: ")

        if nome_remover in agenda_telefonica:
            del agenda_telefonica[nome_remover]
            print(f"Contato '{nome_remover}' removido da agenda.")
        else:
            print(f"Contato '{nome_remover}' não encontrado na agenda.")

    else:
        print("Opção inválida. Por favor, escolha '1', '2', '3' ou 'sair'.")

# Exibe a agenda telefônica ao encerrar o programa
print("\nAgenda Telefônica Final:")
for nome, numero in agenda_telefonica.items():
    print(f"{nome}: {numero}")


