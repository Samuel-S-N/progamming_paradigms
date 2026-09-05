class Hospedagem:
    
    def __init__(self, nome, valorDiaria):
        self.__nome = nome
        self.__valorDiaria = valorDiaria
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def diaria(self):
        return self.__valorDiaria

class Hotel(Hospedagem):
    
    def __init__(self,nome, valorDiaria, cidade, estado):
        super().__init__(nome, valorDiaria)
        self.cidade = Endereco(cidade, estado)

    def reservar(self):
        print("Reserva realizada no hotel.")

class Pousada(Hospedagem):
    
    def __init__(self,nome, valorDiaria, cidade, estado):
        super().__init__(nome, valorDiaria)
        self.cidade = Endereco(cidade, estado)

    def reservar(self):
        print("Reserva realizada na pousada.")

class Endereco:

    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def estado(self):
        return self.__estado

hospedagens = [
    Hotel("Hotel Brasil", 100, "São Paulo", "SP"),
    Pousada("Pousada do Brasil", 50, "Rio de Janeiro", "RJ")
]

for hospedagem in hospedagens:
    hospedagem.reservar()