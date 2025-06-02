#Celso Comuniam Pereira
#Ruylis Bialta

class Diario_de_bordo: #Criação da classe Diario_de_bordo

    def __init__(self, viagens, datas, locais): #Criado a definições para viagens, data e locais  
        try: #Faz a tentativa de inserção dos comandos abaixo    
            self.viagens = viagens 
            self.datas = datas
            self.locais = locais
            print("Informações cadastradas com sucesso!") #Exibe informação de cadastros realizados com sucesso
        except ValueError as e: #Faz o tratamento em caso de erro
            print(f"Erro ao cadastrar: {e}")

    def cadastro(self, experiencia, foto): #Crado definições para experiência e foto
        self.experiencia = experiencia
        self.__foto = foto
        #Abaixo criado um return para exibir as informações dos dados das definições
        return f"Viagem número {self.viagens}, em {self.datas}, para {self.locais}, experiência {self.experiencia}, cod das fotos {self.__foto}"

#Abaixo realizado cadastro de novo usuario
class Novo_usuario: 
    def __init__(self):
        self.usuarios = []
    def adicionar_usuario(self, datas, locais_visitados):
        try:
            nomo_usuario = Novo_usuario(datas, locais_visitados)
            self.usuarios.append(Novo_usuario)
            print("viagem !")
        except ValueError as e:
            print(f"erro na viagem {e}")
    def listar_usuario(self):
        for usuario in self.usuarios:
            print(f"Nome: {usuario()}")

# Atribuição das informações para exibição no return
usuario = Novo_usuario()
viagem1 = Diario_de_bordo (23, "23/01/2025", "Lisboa") 
print(viagem1.cadastro("boa", 123)) 

 
 