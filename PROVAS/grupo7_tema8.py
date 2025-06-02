# FEITO POR: FELIPE FERREIRA DE FRANÇA  | Grupo 7 Tema 8 |


#8 - Sistema de Gerenciamento de Estacionamento
#Controla a entrada e saída de veículos em vagas de estacionamento. Deve registrar horário de 
#entrada, saída e calcular o valor a ser pago com base no tempo de permanência. Também pode listar placa_saida, hora_saida, dia_saida, vaga_vazia
#vagas livres e ocupadas.self.placa_saida=placa_saidaself.hora_saida=hora_saidaself.dia_saida=dia_saidaself.vaga_vazia=vaga_vazia



#Aqui crio a classe Estacionamento, aqui é onde seram registradas a placa do veiculo, horario da entrada, dia da entrada e a vaga na qual esta ocupando
class Estacionamento:
    def __init__ (self, placa_entrada, hora_entrada, dia_entrada, vaga_ocupada):
        self.placa_entrada=placa_entrada
        self.hora_entrada=hora_entrada
        self.dia_entrada=dia_entrada
        self.vaga_ocupada=vaga_ocupada
    
#Aqui o programa pega a quantidade de caracteres dos itens abaixo, se for maior que o permitido o programa não roda e aparece erro ao usuário, senão vai rodar normalmente
#Fazendo com que seja possível também mostrar na tela para o usuário todos os itens necessários
    def get_placa_entrada(self):
        return self.placa_entrada
    def get_hora_entrada(self):
        return self.hora_entrada
    def get_dia_entrada(self):
        return self.dia_entrada
    def get_vaga_ocupada(self):        
        return self.vaga_ocupada
#Se a hora for menor ou igual a 24 horas da noite o programa roda, se não aparece erro
    def set_hora_entrada(self, nova_hora_entrada):
        if (nova_hora_entrada) <=24:
            self.hora_entrada=nova_hora_entrada
        elif (nova_hora_entrada) >= 1:
            self.hora_entrada=nova_hora_entrada
        else:
            raise ValueError("A hora de um dia deve conter 24 digitos para ter a entrada ou saida valida!")
#Se o dia for menor ou ifual a 30 o código roda, se não aparece erro
    def set_dia_entrada(self, nova_dia_entrada):
        if (nova_dia_entrada) <= 30 :
            self.dia_entrada=nova_dia_entrada
        if (nova_dia_entrada) >= 1 :
            self.dia_entrada=nova_dia_entrada
        else:
            raise ValueError("A quantidade de vagas vai é de 99!")
#Se a vaga passar de 2 digitos, não vai rodar e vai dar erro
    def set_vaga_ocupada(self, nova_vaga_ocupada):
        if len (nova_vaga_ocupada) <=2 :
            self.vaga_ocupada=nova_vaga_ocupada
        if len (nova_vaga_ocupada) >=1 :
            self.vaga_ocupada=nova_vaga_ocupada
        else:
            raise ValueError("A placa de um veiculo deve conter sete|7 digitos para ter a entrada ou saida valida!")
#A placa deve conter 7 digitos, se tiver menos ou mais vai dar erro
    def set_placa_entrada(self, nova_placa_entrada):
        if len (nova_placa_entrada) == 7 :
            self.placa_entrada=nova_placa_entrada
        else:
            raise ValueError("A placa de um veiculo deve conter 7 digitos para ter a entrada ou saida valida!")

#O "Sistema" armazena os atributos que foram criados na classe estacionamento em uma lista e depois mostra na tela todos os itens no qual coloquei
class Sistema:
    def __init__(self):
        self.estacionam = []
    def adicionar_placa(self, placa_entrada, hora_entrada, dia_entrada, vaga_ocupada):
        try:
            nova = Estacionamento(placa_entrada, hora_entrada, dia_entrada, vaga_ocupada)
            self.estacionam.append(nova)
            print("Entrada | Saida realizada com sucesso!")
        except ValueError as e:
            print(f"Erro ao realizar o cadastro: {e}")
    def listar_entradas(self):
        for entra_sai in self.estacionam:
            print(f"Placa: {entra_sai.get_placa_entrada()} | Entrou as {entra_sai.get_hora_entrada()} horas | Dia: {entra_sai.get_dia_entrada()} | Vaga: {entra_sai.get_vaga_ocupada()}")
    def listar_saidas(self):
        for entra_sai in self.estacionam:
            print(f"Placa: {entra_sai.get_placa_entrada()} | Saiu as {entra_sai.get_hora_entrada()} horas | Dia: {entra_sai.get_dia_entrada()} | Vaga: {entra_sai.get_vaga_ocupada()}")

#Aqui o programa chama a classe "Sistema" e mostra as placas de veiculos que entraram ou sairam no estacionamento da classe "Estacionamento"

#Entrada do veículo, vai mostrar placa, hora da entrada do veiculo, dia da entrada, vaga que ocupa:
sistema = Sistema()
sistema.adicionar_placa(1234567, 17, 12, 111)
sistema.listar_entradas()

#Sáida do veículo, vai mostrar placa, hora da saida do veiculo, dia da saida, vaga que foi liberada:
sistema = Sistema()
sistema.adicionar_placa(1234567, 12, 14, 111)
sistema.listar_saidas()

