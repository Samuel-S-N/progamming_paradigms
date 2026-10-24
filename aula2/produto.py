class Produto:
    def __init__(self, nome, preco, quantidade):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def get_quantidade(self):
        return self._quantidade

    def calcular_subtotal(self):
        return self._preco * self._quantidade
