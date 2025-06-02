'''PROVA DE PYTHON - 12/05/2025  |  Erika Anastacio Creatto | Matheus Henrique de C. Rumão
12 - Sistema de Aluguel de Filmes ou Séries - Permite listar títulos disponíveis, realizar aluguel (com controle de disponibilidade) e devolver após um período simulado.
'''
#Criação da classe Locadora, com alguns metodos
class Locadora:

#inicializando com o metodo construtor init
    def __init__(self, titulo, categoria):
        self.__titulo = titulo
        self.__categoria = categoria

    Filmes = []

    def adicionar_filmes(self):
            #Tratando o erro com Try/except
            try:
                novo = (self.__titulo , self.__categoria)
                self.Filmes.append(novo)
                print('Filme Cadastrado com sucesso! ') 
            except  ValueError as error:
                print(f'Erro ao cadastrar {error}')
    
    #metodo criado para adicionar um novo filme
    def set_titulo(self, novo_titulo):
        if len(novo_titulo) > 0:
            self.__titulo = novo_titulo
        else:
            raise ValueError("Nome não pode ser vazio.") #verificando se o titulo ja existe
        
    def listar_filmes(self):
         print(f'Os filmes cadastrados são: {self.Filmes}')

####
         
#Criação da Classe Locação com o método construtor init
class Locacao:
    def __init__(self, nome, quantidade, periodo, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.periodo = periodo
        self.valor = valor

# Metodo para realizar locação, contendo tratamento de erros com raise
    def realizar_locacao(self):
        self.quantidade = int(input('Digite a quantidade de filmes escolhidos: '))
        if self.quantidade < 0:
            raise ValueError('A quantidade precisa ser maior do que Zero')
        print(f'Filmes adicionados: {self.quantidade}')

#Método para registrar a venda, apresentando nome do cliente, quantidade de filmes e o pagamento
    def realizar_pagamento(self):
        self.apagar = self.quantidade * self.valor
        print(f'Nome: {self.nome}\nTotal de filmes: {self.quantidade} | Valor a pagar R$: {self.apagar:.2f} | Período de Locação: {self.periodo} dias')



#Criação dos objetos - Filmes da Locadora
filme1 = Locadora("It a coisa", "Terror")
filme2 = Locadora("Harry Potter", "Aventura")
filme3 = Locadora("Morte na Mesopotâmia", "Suspense")
filme4 = Locadora("A culpa é das estrelas", "Drama")
filme5 = Locadora("Comer, rezar e amar", "Romance")

filme1.adicionar_filmes() #Adicionando filmes
filme1.listar_filmes() #Listando filmes

filme2.adicionar_filmes()
filme2.listar_filmes()

filme3.adicionar_filmes()
filme3.listar_filmes()

filme4.adicionar_filmes()
filme4.listar_filmes()

filme5.adicionar_filmes()
filme5.listar_filmes()

#Visualizando cadastro e finalização da locação: Com nome do cliente, quantidade de filmes, período de locação e valor do pagamento.
cliente1 = Locacao('João Marcos', 5, '10', 30)
cliente1.realizar_locacao()
cliente1.realizar_pagamento()

cliente2 = Locacao('Márcia Ap. de Freitas', 2, '10', 30)
cliente2.realizar_locacao()
cliente2.realizar_pagamento()

cliente3 = Locacao('Matheus Socorro', 4, '10', 30)
cliente3.realizar_locacao()
cliente3.realizar_pagamento()