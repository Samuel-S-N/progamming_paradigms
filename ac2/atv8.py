class Entrega:
    
    def __init__(self, destino, peso):
        self.__destino = destino
        self.__peso = peso
    
    @property
    def destino(self):
        return self.__destino
    
    @property
    def peso(self):
        return self.__peso

class EntregaMoto(Entrega):
    
    def __init__(self,destino, peso, entregador):
        super().__init__(destino, peso)
        self.entregador = Entregador(entregador)

    def realizarEntrega(self):
        print("Entrega sendo realizada de moto.")

class EntregaCaminhao(Entrega):
    
    def __init__(self,destino, peso, entregador):
        super().__init__(destino, peso)
        self.entregador = Entregador(entregador)

    def realizarEntrega(self):
        print("Entrega sendo realizada de caminhão.")

class Entregador:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

entregas = [
    EntregaMoto("Barueri - SP", 10, "José"),
    EntregaCaminhao("Fortaleza - CE", 500, "Valmir")
]

for entrega in entregas:
    entrega.realizarEntrega()