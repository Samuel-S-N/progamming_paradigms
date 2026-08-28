class ContaBancaria:
    
    def __init__(self, valor):
        
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, dinheiro):
        if dinheiro > 0:
            self.__valor += dinheiro
        else:
            self.__valor

cb1 = ContaBancaria(1000)

print(cb1.valor)
cb1.valor = 10000
print(cb1.valor)



