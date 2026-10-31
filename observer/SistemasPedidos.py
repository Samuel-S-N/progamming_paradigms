from abc import ABC, abstractmethod

class PedidoObserver(ABC):
    @abstractmethod
    def atualizar(self, mensagem):
        pass

class EmailObserver(PedidoObserver):
    def atualizar(self, mensagem):
        print(f"Email: {mensagem}")

class EstoqueObserver(PedidoObserver):
    def atualizar(self, mensagem):
        print(f"Estoque: {mensagem}")

class FinanceiroObserver(PedidoObserver):
    def atualizar(self, mensagem):
        print(f"Financeiro: {mensagem}")

class Pedido:
    def __init__(self):
        self.__observadores = []
    
    def adicionar_observer(self, observer: PedidoObserver):
        self.__observadores.append(observer)
    
    def remover_observer(self, observer: PedidoObserver):
        self.__observadores.remove(observer)

    def notificar(self, mensagem):
        for observer in self.__observadores:
            observer.atualizar(mensagem)

    def confirmar(self):
        print("Pedido confirmado")
        self.notificar("Novo pedido realizado")

pedido = Pedido()

pedido.adicionar_observer(EmailObserver())
pedido.adicionar_observer(EstoqueObserver())
pedido.adicionar_observer(FinanceiroObserver())

pedido.confirmar()