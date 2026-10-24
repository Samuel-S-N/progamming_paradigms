from strategies.desconto import DescontoStrategy


class DescontoComum(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.05


class DescontoVIP(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.10


class DescontoPremium(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.20


# Extensibilidade: nova estratégia sem alterar Pedido nem ProcessadorPedido
class DescontoEspecial(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.15
