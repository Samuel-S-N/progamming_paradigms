class Instrumento:

    def __init__ (self, nome, marca):
        self.__nome = nome
        self.__marca = marca

    @property
    def nome(self):
        return self.__nome
    
    @property
    def marca(self):
        return self.__marca

class Violao (Instrumento):

    def __init__(self, nome, marca, nomeMusico):
        super().__init__(nome, marca)
        self.musico = Musico(nomeMusico)

    def tocar(self):
        print(f"O violão de {self.musico.nome}, {self.nome}, está sendo tocado")

class Piano (Instrumento):

    def __init__(self,nome, marca, nomeMusico):
        super().__init__(nome, marca)
        self.musico = Musico(nomeMusico)

    def tocar(self):
        print(f"O piano de {self.musico.nome}, {self.nome}, está sendo tocado")

class Musico:
    
    def __init__(self, nome):
        self.__nome  = nome

    @property
    def nome(self):
        return self.__nome

    

Instrumentos = [
    Violao("lespaul", "gibson", "Samuel"),
    Piano("P45", "Yamaha", "Vieira")
]

for instrumento in Instrumentos:
    instrumento.tocar()


