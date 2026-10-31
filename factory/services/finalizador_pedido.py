from models.pedido import Pedido
from pagamentos.pagamento import Pagamento


class FinalizadorPedido:
    def __init__(self, pedido: Pedido, pagamento: Pagamento):
        self.__pedido = pedido
        self.__pagamento = pagamento

    def finalizar(self):
        if self.__pedido.confirmado:
            print(f"Pedido {self.__pedido.numero} ja foi confirmado e pago!")
            return False

        print("Processando pagamento...")
        if not self.__pagamento.pagar(self.__pedido.total()):
            print("Pagamento recusado! Pedido nao confirmado.")
            return False

        print("Pagamento aprovado!")
        self.__pedido.confirmar()
        print(f"Pedido {self.__pedido.numero} confirmado!")

        print("\n========== NOTIFICAÇÕES ==========")
        self.__pedido.notificar("confirmado")
        return True
