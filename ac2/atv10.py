class Servico:
    
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor(self):
        return self.__valor

class ServicoLimpeza(Servico):
    
    def __init__(self,descricao, valor, profissional):
        super().__init__(descricao, valor)
        self.profissional = Profissional(profissional)

    def realizarServico(self):
        print("Executando serviço de limpeza.")

class ServicoManutencao(Servico):
    
    def __init__(self,descricao, valor, profissional):
        super().__init__(descricao, valor)
        self.profissional = Profissional(profissional)

    def realizarServico(self):
        print("Executando serviço de manutenção.")

class Profissional:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

servicos = [
    ServicoLimpeza("Limpeza de escritório", 100, "João"),
    ServicoManutencao("Manutenção de computador", 50, "Maria")
]

for servico in servicos:
    servico.realizarServico()