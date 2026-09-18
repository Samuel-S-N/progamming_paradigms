from abc import ABC, abstractmethod


class veiculos(ABC):
    @abstractmethod
    def abastecer(self):
        pass

class veiculoeletricos(ABC):
    @abstractmethod
    def carregar(self):
        pass

class carro(veiculos):
    def abastecer(self):
        print("Abastecendo mooto...")

class CarroEletrico(veiculoeletricos):
    def carregar(self):
        print("Carregando carro elétrico...")