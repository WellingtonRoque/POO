#Código criado por Airton A. B. Júnior e Pedro Vinicius R. de Souza
#Grupo 03 questão 01

from datetime import datetime
# utilizado para podermos usar os comandos de data: %d-%m-%Y

# É Criado uma classe chamada tarefa para definirmos o titulo, categoria e prazo;
# é também utilizado para definirmos estados de conclusão das tarefas
class Tarefa:
    def __init__(self, titulo, categoria, prazo):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__prazo = datetime.strptime(prazo, "%d-%m-%Y")
        self.__concluida = False

    def marcar_concluida(self):
        self.__concluida = True

    def __str__(self):
        status = "Concluída" if self.__concluida else "Pendente"
        return f"Título: {self.__titulo} | Categoria: {self.__categoria} | Prazo: {self.__prazo.date()} | Status: {status}"
    #A bio que utilizei é uma bio que tive contato corriqueiro apenas, ou seja, ainda possuo pouco dominio sobre ela
    #Infelizmente, devido a esse fato, não pude mudar a ordem do display da data
    #consequentemente, por mais que pessa para inseir uma data no formato dd-mm-aaaa
    #A data a ser mostrada no menu ainda irá estar na formatação aaaa-mm-dd

    def get_titulo(self):
        return self.__titulo

    def get_categoria(self):
        return self.__categoria

    def get_prazo(self):
        return self.__prazo

    def esta_concluida(self):
        return self.__concluida

#A classe abaixo é criado para gerenciar as tarefas de tal maneira que os dados possam interafir com o menu criado logo em seguida
#Além disso, ele é responsável por definir certas mensagens de erro caso sejam inseridos dados errôneos
class GerenciadorDeTarefas:
    def __init__(self):
        self.__tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.__tarefas.append(tarefa)

    def listar_tarefas(self):
        if not self.__tarefas:
            print("\nNenhuma tarefa cadastrada.")
        for i, tarefa in enumerate(self.__tarefas):
            print(f"\n{i + 1}. {tarefa}")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.__tarefas):
            del self.__tarefas[indice]
        else:
            print("\nÍndice inválido.")

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.__tarefas):
            self.__tarefas[indice].marcar_concluida()
        else:
            print("\nÍndice inválido.")

#Menu simples criado para que o usuário possa facilmente interagir com o sistema de maneira clara e concisa
def menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Marcar como Concluída")
    print("0. Sair")

gerenciador = GerenciadorDeTarefas()

#Função criada para que possamos inserir os dados necessários que serão mostrados utilizando o menu acima
#Possui certa funcionabilidade na mostragem e reportagem de dados errôneos inseridos
while True:
    menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        titulo = input("Título: ")
        categoria = input("Categoria: ")
        prazo = input("Prazo (DD-MM-AAAA): ")
        tarefa = Tarefa(titulo, categoria, prazo)
        gerenciador.adicionar_tarefa(tarefa)

    elif opcao == "2":
        gerenciador.listar_tarefas()

    elif opcao == "3":
        gerenciador.listar_tarefas()
        indice = int(input("\nDigite o número da tarefa a remover: ")) - 1
        gerenciador.remover_tarefa(indice)

    elif opcao == "4":
        gerenciador.listar_tarefas()
        indice = int(input("\nDigite o número da tarefa a concluir: ")) - 1
        gerenciador.marcar_concluida(indice)

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("\nOpção inválida.")

#PS. como ainda não possuo total domínio desta biblioteca eu infelizmente nao fui capaz de criar uma exceção e mensagem de erro clara caso seja inserido uma data que não encaixe com o formato desejado
