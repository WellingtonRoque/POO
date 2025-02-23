while True:
    # Exibe o menu
    print("\nMenu de Opções:")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("4 - Sair")

    # Solicita a escolha do usuário
    escolha = input("Escolha uma opção (1-4): ")

    # Verifica a opção escolhida
    if escolha == "1":
        print("Você escolheu a Opção 1.")
    elif escolha == "2":
        print("Você escolheu a Opção 2.")
    elif escolha == "3":
        print("Você escolheu a Opção 3.")
    elif escolha == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção entre 1 e 4.")
