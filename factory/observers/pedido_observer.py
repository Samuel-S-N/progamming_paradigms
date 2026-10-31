from abc import ABC, abstractmethod


class PedidoObserver(ABC):
    @abstractmethod
    def atualizar(self, mensagem):
        pass
