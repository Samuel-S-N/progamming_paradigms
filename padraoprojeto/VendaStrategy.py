from abc import ABC, abstractmethod

class DescontoStrategy(ABC):
    @abstractmethod
    def calcular(self):
        pass

class DescontoComum(DescontoStrategy):
    def calcular(self):
        return 0.05

class DescontoVip(DescontoStrategy):
    def calcular(self):
        return 0.10

class DescontoPremium(DescontoStrategy):
    def calcular(self):
        return 0.20

class Venda:
    def __init__(self, desconto: DescontoStrategy):
        self.desconto = desconto
        

    def calcular_valor_final(self, valor):
        return valor - (valor * self.desconto.calcular())

    def mudar_desconto(self, novoDesconto: DescontoStrategy):
        self.desconto = novoDesconto

venda = Venda(DescontoComum())

print(f"Desconto comum: R${venda.calcular_valor_final(100)}")

venda.mudar_desconto(DescontoPremium())
print(f"Desconto Premium: R${venda.calcular_valor_final(100)}")