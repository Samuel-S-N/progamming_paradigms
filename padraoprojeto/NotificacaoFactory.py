from abc import ABC, abstractmethod

class NotificacaoFactory(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass

class Email(NotificacaoFactory):
    def enviar(self, mensagem):
        print(f"Email enviado: {mensagem}")
    
class SMS(NotificacaoFactory):
    def enviar(self, mensagem):
        print(f"SMS enviado: {mensagem}")

class NotificacaoCreator(ABC):
    @abstractmethod
    def criar_notificacao(self) -> NotificacaoFactory:
        pass

    def notificar(self, mensagem):
        notificacao = self.criar_notificacao()
        notificacao.enviar(mensagem)

class EmailCreator(NotificacaoCreator):
    def criar_notificacao(self) -> NotificacaoFactory:
        return Email()
    pass

class SMSCreator(NotificacaoCreator):
    def criar_notificacao(self) -> NotificacaoFactory:
        return SMS()

email = EmailCreator()
sms = SMSCreator()

email.notificar("Pedido enviado")
sms.notificar("Erik matador de cavalo")