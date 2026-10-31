from pagamentos.pagamento import Pagamento
from pagamentos.gateway_boleto import GatewayBoleto


class BoletoAdapter(Pagamento):
    def __init__(self, gateway: GatewayBoleto):
        self.__gateway = gateway

    def pagar(self, valor):
        return self.__gateway.emitir_boleto(valor)
