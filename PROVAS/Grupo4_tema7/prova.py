""" GRUPO4: 7 - Sistema de Agendamento de Consultas Médicas
Permite cadastrar pacientes, médicos e horários disponíveis. O sistema deve permitir agendar, 
cancelar e listar consultas. Também pode validar conflitos de horários e permitir consultas por 
paciente."""
#joão Emanoel e Elisangela



#Criando a class do pacientes e seus atributos
class Paciente:
    def __init__(self,nome, idade, rg):
        self.nome = nome 
        self.idade = idade
        self.rg = rg
        
#validado servira para validar se o usuario digitou um seu rg.
    def validado(self,cpf):
        if len(cpf) > 0:
           self.__rg = cpf
        else:
            raise ValueError("Digite um RG valido")

#Criando a class agendamento com seus atributos como 
#paciente: criando a class do paciente para realizar seu cadastro. 
class Agendamento:
    def __init__(self,):
        self.paciente = []
  
#medico: medico colocamos um def para colocar suas informação e seu crm colocar como protegido.
    def medico(self, nome, crm):
        self.nome = nome 
        self.crm = crm 

#Data serve para cadastrar as horas, o dia e mes
    def data(self, horas, dia, mes):
        self.horas = horas
        self.dia = dia
        self. mes = mes

#Adicionando consultar
    def consultar(self,cpf, crm, dia, horas):
        try:
            usuario = Paciente(cpf) 
            self.paciente(usuario)
            profisional = medico(crm)
            self.medico(profisional)
            horario = data(dia, horas) 
            self.data(horario)
            print("Consulta agendada com sucesso: ")
        except ValueError as e:
            print(f"Erro ao cadastrar: {e}")

#Colocando tudo em consulta na lista
    def lista_Consultar(self):
        for consultar in self.paciente, self.medico, self.data:
            print(f"cpf; {consultar.cpf}/n crm; {consultar.profisional}/n data; {consultar.horario}/n")

#Ser a hora for a mesma, sera mandado para reagendar
    def reagendar(self):
        if  self.horas == self.horas:
            print ("Esse horario já está agendado para outro usuario")
        else:
            print("Esse é seu horario")

#Execução
agendamento = Agendamento()
agendamento.lista_Consultar.usuario("Gustavo","12","454987")
agendamento.lista_Consultar.profisional("maria","7678-0")
agendamento.lista_Consultar.horario("11:00h","10","2")

agendamento.lista_Consultar()




    

        

        

        
        

    

    
    
    


        
