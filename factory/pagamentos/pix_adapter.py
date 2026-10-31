from pagamentos.pagamento import Pagamento
from pagamentos.gateway_pix import GatewayPix


class PixAdapter(Pagamento):
    def __init__(self, gateway: GatewayPix):
        self.__gateway = gateway

    def pagar(self, valor):
        return self.__gateway.transferir(valor)
