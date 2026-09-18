
# originalmente, pedido era resposável por calcular o valor, salvar no repositório e enviar o email
# esse acumulo de funções viola o SRP, pois ele define que uma classe, deve ter apenas uma função.

class Pedido():
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

    def calcular_total(self):
        return self.valor * 1.10

# responsabilidades que o SRP pede pra separar. elas só recebem o pedido como parâmetro.

class PedidoRepository():

    def salvar(self, pedido):
        print("Salvando pedido no banco de dados...")

class EmailService():
    def enviar_email(self, pedido):
        print(f"Enviando confirmação para {pedido.cliente}...")


if __name__ == "__main__":
    pedido = Pedido("João", 100)
    print(f"Total do pedido: {pedido.calcular_total():.2f}")

    repository = PedidoRepository()
    repository.salvar(pedido)

    email_service = EmailService()
    email_service.enviar_email(pedido)
