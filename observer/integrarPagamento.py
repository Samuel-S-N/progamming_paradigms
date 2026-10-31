from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

#serviço externo

class GatewayExterno:
    def realizar_transacao(self, quantia):
        print(f"Transacao externa de R${quantia:.2f}")

class GatewayAdapter(Pagamento):
    def __init__(self, gateway: GatewayExterno):
        self.__gateway = gateway

    def pagar(self, valor):
        self.__gateway.realizar_transacao(valor)

class Venda:
    def __init__(self, pagamento: Pagamento):
        self.__pagamento = pagamento
        
    def finalizar(self, valor):
        self.__pagamento.pagar(valor)

gateway = GatewayExterno()
adapter = GatewayAdapter(gateway)

venda = Venda(adapter)

venda.finalizar(200.00)