from observers.pedido_observer import PedidoObserver


class EmailObserver(PedidoObserver):
    def __init__(self, pedido):
        self.__pedido = pedido

    def atualizar(self, mensagem):
        print("EMAIL:")
        print(f"{self.__pedido.cliente}, seu pedido foi {mensagem}.")
