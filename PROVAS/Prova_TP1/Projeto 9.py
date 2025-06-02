# Gerencia cursos, alunos e inscrições. Permite listar cursos disponíveis, inscrever alunos, registrar a 
# conclusão de cursos e gerar certificados simples. Pode incluir categorias de cursos e progresso do 
# aluno

# Criação de classe
class Aluno:

    # Criação de atributos
    def __init__(self, nome, email, curso):
        self.__nome = nome
        self.__email = email
        self.__curso = curso

    # Adicionar as informações dos alunos
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def lista_curso(self):
        return self.__curso

    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            raise ValueError("Não registrado")
        
# Criação da segunda classe
class Inscrição:

    # Gerenciar os métodos dos alunos
    def __init__(self):
        self.usuarios = []

    def cadastrar_aluno(self, nome, email, curso):
        try:
            novo = Aluno(nome, email, curso)
            self.usuarios.append(novo)
            print("Aluno cadastrado!")
            
        except ValueError as erro:
            print(f"Erro detectado: {erro}")

    def  não_cadastrar_aluno(self, nome, email, curso):
        try:
            novo = Aluno(nome, email, curso)
            self.usuarios.append(novo)
            print("Aluno não cadastrado")
        
        except ValueError as erro:
            print(f"Erro detectado: {erro}")



    def listar_alunos(self):
        for usuario in self.usuarios:
            print("Certificado da faculdade APROVADO")
            print(f"Nome: {usuario.get_nome()}")
            print(f"Email: {usuario.get_email()}")
            print(f"Curso: {usuario.lista_curso()}")
            print(f"-----")


# Criação de objetos
aluno1 = Inscrição()
aluno1.cadastrar_aluno("alan", "alan@gmail.com", "Inglês")
aluno1.listar_alunos()

aluno2 = Inscrição()
aluno2.cadastrar_aluno("Roberto", "roberto@icloud.com", "Informática")
aluno2.listar_alunos()

# Execução
"""
Aluno cadastrado!
Certificado da faculdade APROVADO
Nome: alan
Email: alan@gmail.com
Curso: Inglês
Aluno cadastrado!
Certificado da faculdade APROVADO
Nome: Roberto
Email: roberto@icloud.com
Curso: Informática 
"""



