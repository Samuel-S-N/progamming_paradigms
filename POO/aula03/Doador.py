class Doador:

    def __init__(self, nome):
        self.nome = nome
        self.__valor = 0
        
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, dinheiro):
        if dinheiro > 0:
            self.__valor += dinheiro
        else:
            self.__valor
            print("o valor deve ser positivo")

    def mostrarDados(self):
        print(self.nome)
        print(self.valor)


d1 = Doador("Samuel")

d1.mostrarDados()

d1.valor = 100

d1.mostrarDados()

d1.valor = -80

d1.mostrarDados()