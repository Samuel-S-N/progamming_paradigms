class Produto:
    def __init__(self, codigo, nome, preco):
        self.__codigo = codigo
        self.__nome = nome
        self.preco = preco

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preco deve ser positivo")
        self.__preco = valor
