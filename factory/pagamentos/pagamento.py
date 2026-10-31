from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass
