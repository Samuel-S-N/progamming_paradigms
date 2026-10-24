from produto import Produto
from strategies.desconto import DescontoStrategy


class Pedido:
    def __init__(self, desconto: DescontoStrategy):
        self._produtos = []
        self._desconto = desconto

    def adicionar_produto(self, produto: Produto):
        self._produtos.append(produto)

    def get_produtos(self):
        return list(self._produtos)

    def calcular_total_bruto(self):
        return sum(p.calcular_subtotal() for p in self._produtos)

    def calcular_desconto(self):
        return self._desconto.calcular(self.calcular_total_bruto())

    def calcular_total_final(self):
        return self.calcular_total_bruto() - self.calcular_desconto()
