#Controle de Treinos em Academia
#Registra alunos, tipos de treinos e frequências semanais. Permite consultar histórico e sugerir treinos.
# Nomes: Bárbara Helena Preto Brandino | Clara Vecchio Machado da Silva | 2º Semestre de DSM
class Registro:
    def __init__(self, nome, idade, treinos, frequencia):
        self.__nome = nome
        self.__idade = idade
        self.__treinos = treinos
        self.__frequencia = frequencia
        #São adicionados os atributos na classe registro, que são necessários para registrar um aluno na academia.
    
    def get(self):
        return self.__nome, self.__idade, self.__treinos, self.__frequencia
        #Por conta dos atributos estarem privados, é necessário o get para poder acessá-los.
    
    def exibir(self):
        if len(self.__nome) > 0 and self.__idade > 0:
            print(f"\nNome do aluno {self.__nome}.\nIdade do aluno: {self.__idade}.\nTipo de treino: {self.__treinos}.\nFrequência semanal: {self.__frequencia}.\n")
        else:
            raise ValueError("Nome/Idade inválidos.")
        #O registro do aluno só será exibido caso siga as condições impostas, ou seja, é obrigatório preencher o campo de nome e inserir uma idade válida, caso contrário, mostrará a mensagem de erro.
        
    def historico(self, treino_antes):
        self.treino_antes = treino_antes
        print("\nHISTÓRICO")
        print(f"Nome do aluno: {self.__nome}.\nTreino anterior: {self.treino_antes}.\n")
        #Poderá adicionar treinos já feitos pelo aluno.

class Sugestao:
    sugestoes = []
    #é criada uma lista de sugestões de treinos vazia.
        
    def exibir_sugestoes(sugestoes):
        print(f"Sugestões de treinos: {sugestoes}")
        #irá mostrar a lista criada.

#objetos criados, com os atributos pedidos.
aluno1 = Registro("Juliano", 24, "Funcional", "4 vezes na semana") 
aluno2 = Registro("Clara", 20, "Natação", "2 vezes na semana")
aluno3 = Registro("Pedro", -10, "Funcional", "1 vez na semana")


aluno1.exibir()
aluno1.historico("Funcional") #mostra os objetos e o histórico

aluno2.exibir() #exibe as informações do aluno
aluno2.historico("Jazz") #mostra os objetos e o histórico

Sugestao.exibir_sugestoes(["CrossFit","Jazz","FitDance","Musculação"]) #lista de sugestões

aluno3.exibir()#exibe as informações do aluno, mas, nesse caso, será mostrado um erro, pois a idade inserida é negativa e não segue os requisitos.