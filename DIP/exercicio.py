from abc import ABC, abstractmethod
#loja virtual

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class EmailNotificador(Notificador):
    def enviar(self, mensagem):
        print(f"Email: {mensagem}")

class SMSNotificador(Notificador):
    def enviar(self, mensagem):
        print(f"SMS: {mensagem}")

class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento no pix. Valor R${valor:.2f}")

class Cartao(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento no cartão. Valor R${valor:.2f}")

class Boleto(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento no boleto. Valor R${valor:.2f}")

class PedidoService():
    def __init__(self, notificador: Notificador, pagamento: Pagamento):
        self.notificador = notificador
        self.pagamento = pagamento

    def finalizar(self, valor):
        self.pagamento.pagar(valor)
        self.notificador.enviar("pedido finalizado com sucesso")


pix = Pix()
cartao = Cartao()
boleto = Boleto()

email = EmailNotificador()
sms = SMSNotificador()

pedido = PedidoService(email, pix)
pedido.finalizar(100)

pedido = PedidoService(sms, cartao)
pedido.finalizar(100)