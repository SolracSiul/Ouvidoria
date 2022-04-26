class Usuario:
    def __init__(self, nome, descricao, tipo):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self,nome):
        self.nome = nome

    @property
    def descricao(self):
        return self.descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.descricao = descricao

    @property
    def tipo(self):
        return self.tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo




















"""
def criar_Usuario():
    nome: str = input("digite seu nome: ")
    descricao: str = input("informe a descricao: ")
    tipo: str = input("informe o tipo: ")

def mostrar(self):
    print("meu nome eh " + self.nome)
    print("minha descricao eh " + self.descricao)
    print("meu tipo eh " + self.tipo)

    criar_Usuario()
print(Usuario)
print(Usuario.mostrar())
"""