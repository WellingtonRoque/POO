print("""
Caio Simonassi e Lucas Corrêa
Grupo 5

10 - Plataforma de Marketplace
Permite cadastrar produtos, vendedores e clientes. Os usuários podem listar produtos disponíveis, 
simular uma compra e ver detalhes de pedidos. O sistema pode incluir carrinho e controle de 
estoque básico.

LOJA DE CAMISETAS
""")

# classe produto com atributos privados e getters e setters para os atributos necessarios
class Produto:
    def __init__(self, id_produto, nome, cor, preco, estoque):
        self.__id_produto = id_produto
        self.__nome = nome
        self.__preco = preco
        self.__cor = cor
        self.__estoque = estoque

    def get_dados(self):
        return f"ID: {self.__id_produto} | NOME: {self.__nome} | COR: {self.__cor} | PREÇO: {self.__preco} | ESTOQUE: {self.__estoque}"

    def get_nome(self):
        return self.__nome

    def get_id(self):
        return self.__id_produto

    def get_preco(self):
        return self.__preco
    def set_estoque(self, quantidade):
        self.__estoque += quantidade

#classe pai usuario
class Usuario:
    def __init__(self, nome, telefone):
        self.__nome = nome

        self.__telefone = telefone

    def altera_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
        else:
            raise ValueError("Nome não pode ser vazio.")

    def get_nome(self):
        return f"NOME: {self.__nome} | TEL: {self.__telefone}"

# classe vendedor que herda de Usuario
class Vendedor(Usuario):
    def __init__(self, id_vendedor, nome, telefone, salario):
        super().__init__(nome, telefone)
        self.id_vendedor = id_vendedor
        self.__salario = salario

    def get_id(self):
        return self.id_vendedor

# classe cliente que Herda de usuario tambem, e tem o carrinho e os pedidos feitos pelo usuario
class Cliente(Usuario):
    def __init__(self, nome, cpf, telefone, email):
        super().__init__(nome, telefone)
        self.__email = email
        self.__cpf = cpf
        self.carrinho = []
        self.pedidos = []

    def get_cpf(self):
        return self.__cpf

    def get_carrinho(self):
        return self.carrinho

    def get_pedido(self):
        return self.pedidos

# classe sistema que gerencia e acessa as outras classes
class Sistema:
    def __init__(self):
        self.clientes = []
        self.vendedores = []
        self.produtos = []
        self.vendas = {}

    def cadastrar_produto(self, id_produto, nome, cor, preco, estoque):
        try:
            new = Produto(id_produto, nome, cor, preco, estoque)
            self.produtos.append(new)
            print("Produto cadastrado!")
        except ValueError:
            print(f"Erro ao cadastrar produto: {ValueError}")

    def cadastrar_cliente(self, nome, cpf, telefone, email):
        try:
            new = Cliente(nome, cpf, telefone, email)
            self.clientes.append(new)
            print(f"Cliente cadastrado com sucesso! Seja bem-vindo a nossa loja!")
        except ValueError:
            print(f"Erro ao cadastrar Cliente: {ValueError}")

    def cadastrar_vendedor(self, id_vendedor, nome, telefone, salario):
        try:
            new = Vendedor(id_vendedor, nome, telefone, salario)
            self.vendedores.append(new)
            print("Vendedor cadastrado com sucesso!")
        except ValueError:
            print(f"Erro ao cadastrar Vendedor: {ValueError}")

    def listar_clientes(self):
        print("Clientes:")
        for cliente in self.clientes:
            print(f"    {cliente.get_nome()}")

    def listar_vendedores(self):
        print("Vendedores:")
        for vendedor in self.vendedores:
            print(f"    {vendedor.get_nome()}")

    def listar_produtos(self):
        print("Produtos:")
        for produto in self.produtos:
            print(f"    {produto.get_dados()}")

    def adiciona_estoque(self, id_produto, quantidade):
        for produto in self.produtos:
            if produto.get_id() == id_produto:
                if quantidade > 0:
                    produto.set_estoque(quantidade)
                    print("Estoque alterado com sucesso!")
                else:
                    raise ValueError("Quantidade não pode ser menor que 0.")

    def remove_estoque(self, id_produto, quantidade):
        for produto in self.produtos:
            if produto.get_id() == id_produto:
                if quantidade < 0:
                    produto.set_estoque(quantidade)
                    print("Estoque alterado com sucesso!")

    def adiciona_carrinho(self, cpf, cod_produto, quantidade):
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                for produto in self.produtos:
                    if produto.get_id() == cod_produto:
                        sys.remove_estoque(cod_produto, quantidade)
                        cliente.carrinho.append(produto.get_nome())
                        cliente.carrinho.append(produto.get_preco())
                        cliente.carrinho.append(-quantidade)
                        print("Produto adicionado ao carrinho.")

    def ver_carrinho(self, cpf):
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                print("Produto | Preco | Quantidade")
                print(cliente.get_carrinho())

    def finaliza_compra(self, cpf):
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                for itens in cliente.carrinho:
                    cliente.pedidos.append(itens)
                cliente.carrinho.clear()

    def ver_pedidos(self, cpf):
        for cliente in self.clientes:
            if cliente.get_cpf() == cpf:
                print(f"Pedidos:")
                print(f"Produto | Preco | Quantidade\n  {cliente.get_pedido()}")


sys = Sistema()

# cadastro dos clientes
sys.cadastrar_cliente("Caio", "12345678910", "0987654321", "caio.cliente@loja.com")
sys.cadastrar_cliente("Gustavo", "13256767578", "12435697867", "gustavo.cliente@loja.com")

#cadastra os vendedores
sys.cadastrar_vendedor(1, "Lucas", "97534031", 2000)
sys.cadastrar_vendedor(2, "Pedro", "454543244312", 1999)

#cadastra produtos
sys.cadastrar_produto(1, "Camiseta Adidas", "Preta", 99.99, 5)
sys.cadastrar_produto(2, "Camiseta Nike", "Roxo", 139.99, 7)

#listagem das classes
sys.listar_clientes()
sys.listar_vendedores()
sys.listar_produtos()

#adiciona produtos ao estoque
sys.adiciona_estoque(1, 20)

sys.listar_produtos()

#adiciona produtos ao carrinho e remove da quantidade do estoque
sys.adiciona_carrinho("12345678910", 2, -1)
sys.adiciona_carrinho("12345678910", 1, -3)
sys.ver_carrinho("12345678910")

sys.listar_produtos()

#finaliza a compra, adiciona os items para os pedidos e apaga o carrinho
sys.finaliza_compra("12345678910")
sys.ver_pedidos("12345678910")
