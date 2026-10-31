from pagamentos.pagamento import Pagamento
from pagamentos.gateway_cartao import GatewayCartao


class CartaoAdapter(Pagamento):
    def __init__(self, gateway: GatewayCartao):
        self.__gateway = gateway

    def pagar(self, valor):
        return self.__gateway.cobrar_cartao(valor)
