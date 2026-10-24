from abc import ABC, abstractmethod


class DescontoStrategy(ABC):
    @abstractmethod
    def calcular(self, valor):
        """Retorna o valor do desconto a ser aplicado sobre `valor`."""
