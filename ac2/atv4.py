class Personagem:
    
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__vida

class Guerreiro(Personagem):
    
    def __init__(self, nome, vida, arma):
        super().__init__(nome, vida)
        self.arma = Arma(arma)

    def atacar(self):
        print("O guerreiro atacou com uma espada.")

class Mago(Personagem):
    
    def __init__(self, nome, vida, arma):
        super().__init__(nome, vida)
        self.arma = Arma(arma)

    def atacar(self):
        print("O mago lançou magia.")

class Arma:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

personagens = [
    Guerreiro("Ferguson", "300", "Excalibur"),
    Mago("Enzo", "150", "Mundus")
]

for personagem in personagens:
    personagem.atacar()