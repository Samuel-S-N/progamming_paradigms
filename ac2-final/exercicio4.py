from abc import ABC, abstractmethod

# o problema original: Notificacao decide o canal de envio com if/elif por tipo,
# então cada canal novo (como o push que vem depois) exige alterar essa classe, violando o OCP.
# a solução cria uma classe abstrata Notificador e uma subclasse por canal, todas com enviar(mensagem).
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass


class Email(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando EMAIL: {mensagem}")


class SMS(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")


class WhatsApp(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando WhatsApp: {mensagem}")


class PushNotification(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando PUSH: {mensagem}")


def enviar_notificacao(notificador, mensagem):
    notificador.enviar(mensagem)


if __name__ == "__main__":
    email = Email()
    sms = SMS()

    enviar_notificacao(email, "Pedido realizado!")
    enviar_notificacao(sms, "Pagamento aprovado!")
    enviar_notificacao(PushNotification(), "Novo pedido no app!")
