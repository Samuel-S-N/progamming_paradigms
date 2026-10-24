from abc import ABC, abstractmethod

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

class PedidoService():
    
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def finalizar(self):
        print("Pedido finalizado")
        self.notificador.enviar("Seu pedido foi finalizado.")

email = EmailNotificador()
sms = SMSNotificador()

pedido = PedidoService(email)
pedido.finalizar()

pedido = PedidoService(sms)
pedido.finalizar()