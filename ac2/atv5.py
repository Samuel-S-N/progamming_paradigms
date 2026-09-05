class Transporte:
    
    def __init__(self, linha, capacidade):
        self.__linha = linha
        self.__capacidade = capacidade
    
    @property
    def linha(self):
        return self.__linha
    
    @property
    def capacidade(self):
        return self.__capacidade

class Onibus(Transporte):
    
    def __init__(self,linha, capacidade, motorista):
        super().__init__(linha, capacidade)
        self.motorista = Motorista(motorista)

    def Transportar(self):
        print("O Onibus está transportante passageiros.")

class Metro(Transporte):
    
    def __init__(self,linha, capacidade, condutor):
        super().__init__(linha, capacidade)
        self.condutor = Condutor(condutor)

    def Transportar(self):
        print("O Metro está transportando passageiros.")

class Motorista:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Condutor:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

transportes = [
    Onibus("459", "50", "Samuel"),
    Metro("Amarela", "1000", "Pedro")
]

for transporte in transportes:
    transporte.Transportar()