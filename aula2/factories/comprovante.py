from abc import ABC, abstractmethod


class Comprovante(ABC):
    @abstractmethod
    def emitir(self, pedido, total):
        pass
