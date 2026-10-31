from observers.pedido_observer import PedidoObserver


class LogObserver(PedidoObserver):
    def __init__(self, pedido, arquivo="notificacoes.txt"):
        self.__pedido = pedido
        self.__arquivo = arquivo

    def atualizar(self, mensagem):
        with open(self.__arquivo, "a", encoding="utf-8") as log:
            log.write(f"Pedido {self.__pedido.numero}: {mensagem}\n")
