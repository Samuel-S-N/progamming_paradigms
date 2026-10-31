from observers.pedido_observer import PedidoObserver


class FinanceiroObserver(PedidoObserver):
    def __init__(self, pedido):
        self.__pedido = pedido

    def atualizar(self, mensagem):
        print("FINANCEIRO:")
        print(f"Pagamento de R$ {self.__pedido.total():.2f} registrado.")
