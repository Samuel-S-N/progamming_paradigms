from abc import ABC, abstractmethod

class Desconto(ABC):

    @abstractmethod
    def calcular(self, valor):
        pass

class Cliente:    
    def __init__(self,tipo):
        self.tipo = tipo

class DescontoComum(Desconto):
    def calcular(self, valor):
        return valor * 0.05

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.10

def aplicar_desconto(desconto, valor):
    return desconto.calcular(valor)

comum = DescontoComum()
premium = DescontoPremium()

valor_compra = 1000

desconto_comum = aplicar_desconto(comum, valor_compra)
desconto_premium = aplicar_desconto(premium, valor_compra)

print(f"{desconto_comum:.2f}")
print(f"{desconto_premium:.2f}")





#class CalcularDesconto(Desconto):
#    
#    def calcular(self, tipoCliente, valor):
#        
#        if tipoCliente == "comum":
#            return valor * 0.05
#        
#        elif tipoCliente == "premium":
#            return valor * 0.10
#
#        elif tipoCliente == "vip":
#            return valor * 0.15

#desconto = CalcularDesconto()

#print(desconto.calcular("comum", 100.00))