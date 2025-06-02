    """
    ALUNO: GUSTAVO BRAVO 
    ALUNO: ANA LÚCIA DA SILVA
    Agenda de Contatos com Etiquetas
    Cadastra contat.nome, telefone e etiquetas (ex: família, trabalho), permitindo buscar e edit	ar.

    
    """

# classe que representa o contato 
class Contato:
    def __init__(self, nome, telefone, etiquetas):
        # atributos privados
        self.__nome = nome
        self.__telefone = telefone
        self.__etiquetas = etiquetas  # Lista de etiquetas 

    # definindo o get e dando return
    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def get_etiquetas(self):
        return self.__etiquetas

    # voltar o erro
    def set_nome(self, novo_nome):
        if novo_nome.strip():
            self.__nome = novo_nome
        else:
            raise ValueError("Nome não pode ser vazio.")

    def set_telefone(self, novo_telefone):
        if novo_telefone.strip():
            self.__telefone = novo_telefone
        else:
            raise ValueError("Telefone não pode ser vazio.")

    def set_etiquetas(self, novas_etiquetas):
        if isinstance(novas_etiquetas, list) and novas_etiquetas:
            self.__etiquetas = novas_etiquetas
        else:
            raise ValueError("Deve fornecer uma lista de etiquetas não vazia.")


# Gerenciamento dos cantatos
class Agenda:
    def __init__(self):
        # adicionar e excluir nome, telefone, e etiqueta
        self.contatos = {}

    def adicionar_contato(self, nome, telefone, etiquetas):
        try:
            if nome in self.contatos:
                raise ValueError("Contato com esse nome já existe.")
            contato = Contato(nome, telefone, etiquetas)
            self.contatos[nome] = contato
            print(f"Contato '{nome}' adicionado com sucesso!")
        except ValueError as e:
            print(f"Erro ao adicionar contato: {e}")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            for nome, contato in self.contatos.items():
                print(f"Nome: {contato.get_nome()}, Telefone: {contato.get_telefone()}, Etiquetas: {', '.join(contato.get_etiquetas())}")

    def buscar_por_etiqueta(self, etiqueta):
        print(f"Contatos com a etiqueta '{etiqueta}':")
        encontrados = False
        for contato in self.contatos.values():
            if etiqueta in contato.get_etiquetas():
                print(f"- {contato.get_nome()} ({contato.get_telefone()})")
                encontrados = True
        if not encontrados:
            print("Nenhum contato encontrado com essa etiqueta.")

    def editar_contato(self, nome, novo_telefone=None, novas_etiquetas=None):
        try:
            if nome not in self.contatos:
                raise ValueError("Contato não encontrado.")
            contato = self.contatos[nome]
            if novo_telefone:
                contato.set_telefone(novo_telefone)
            if novas_etiquetas:
                contato.set_etiquetas(novas_etiquetas)
            print(f"Contato '{nome}' atualizado com sucesso!")
        except ValueError as e:
            print(f"Erro ao editar contato: {e}")

    def remover_contato(self, nome):
        try:
            if nome in self.contatos:
                del self.contatos[nome]
                print(f"Contato '{nome}' removido com sucesso!")
            else:
                raise ValueError("Contato não encontrado.")
        except ValueError as e:
            print(f"Erro: {e}")


# demonstração do uso
agenda = Agenda()
agenda.adicionar_contato("Ana", "1111-2222", ["família"])
agenda.adicionar_contato("Carlos", "3333-4444", ["trabalho", "amigos"])
agenda.adicionar_contato("Beatriz", "5555-6666", ["trabalho"])

print("\n Lista de contatos ")
agenda.listar_contatos()

print("\n Buscar por etiqueta 'trabalho' ")
agenda.buscar_por_etiqueta("trabalho")

print("\n Editar contato 'Carlos' ")
agenda.editar_contato("Carlos", novo_telefone="7777-8888", novas_etiquetas=["trabalho", "esporte"])

print("\n Lista após edição ")
agenda.listar_contatos()

print("\n Remover contato 'Ana' ")
agenda.remover_contato("Ana")

print("\n Lista final ")
agenda.listar_contatos()
