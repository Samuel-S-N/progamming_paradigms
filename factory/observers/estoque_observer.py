from observers.pedido_observer import PedidoObserver


class EstoqueObserver(PedidoObserver):
    def __init__(self, pedido):
        self.__pedido = pedido

    def atualizar(self, mensagem):
        print("ESTOQUE:")
        print(f"Separar os produtos do pedido {self.__pedido.numero}.")
