class Prato:
    
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco

class PratoPrincipal(Prato):
    
    def __init__(self,nome, preco, cozinheiro):
        super().__init__(nome, preco)
        self.cozinheiro = Cozinheiro(cozinheiro)

    def Preparar(self):
        print("Preparando o prato principal.")

class Sobremesa(Prato):
    
    def __init__(self,nome, preco, cozinheiro):
        super().__init__(nome, preco)
        self.cozinheiro = Cozinheiro(cozinheiro)

    def Preparar(self):
        print("Preparando a sobremesa.")

class Cozinheiro:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

pratos = [
    PratoPrincipal("Risoto", "50", "Samuel"),
    Sobremesa("Sorvete", "30", "Eduarda")
]

for prato in pratos:
    prato.Preparar()