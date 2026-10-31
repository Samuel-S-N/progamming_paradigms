from observers.pedido_observer import PedidoObserver


class Pedido:
    def __init__(self, numero, cliente, produtos, endereco="", observacoes=""):
        self.__numero = numero
        self.__cliente = cliente
        self.__produtos = list(produtos)
        self.__endereco = endereco
        self.__observacoes = observacoes
        self.__confirmado = False
        self.__observadores = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def produtos(self):
        return list(self.__produtos)

    @property
    def endereco(self):
        return self.__endereco

    @property
    def observacoes(self):
        return self.__observacoes

    @property
    def confirmado(self):
        return self.__confirmado

    def total(self):
        return sum(produto.preco for produto in self.__produtos)

    def confirmar(self):
        if self.__confirmado:
            raise ValueError(f"Pedido {self.__numero} ja foi confirmado")
        self.__confirmado = True

    def adicionar_observer(self, observer: PedidoObserver):
        self.__observadores.append(observer)

    def remover_observer(self, observer: PedidoObserver):
        self.__observadores.remove(observer)

    def notificar(self, mensagem):
        for observer in self.__observadores:
            observer.atualizar(mensagem)
