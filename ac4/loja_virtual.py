from abc import ABC, abstractmethod

# PRODUTO
class Produto:
    def __init__(self, codigo, nome, preco):
        self.__codigo = codigo
        self.__nome = nome
        self.preco = preco

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O preco deve ser positivo")
        self.__preco = valor

# OBSERVER
class PedidoObserver(ABC):
    @abstractmethod
    def atualizar(self, mensagem):
        pass

class EmailObserver(PedidoObserver):
    def __init__(self, pedido):
        self.__pedido = pedido

    def atualizar(self, mensagem):
        print("EMAIL:")
        print(f"{self.__pedido.cliente}, seu pedido foi {mensagem}.")

class EstoqueObserver(PedidoObserver):
    def __init__(self, pedido):
        self.__pedido = pedido

    def atualizar(self, mensagem):
        print("ESTOQUE:")
        print(f"Separar os produtos do pedido {self.__pedido.numero}.")

class FinanceiroObserver(PedidoObserver):
    def __init__(self, pedido):
        self.__pedido = pedido

    def atualizar(self, mensagem):
        print("FINANCEIRO:")
        print(f"Pagamento de R$ {self.__pedido.total():.2f} registrado.")

class LogObserver(PedidoObserver):
    def __init__(self, pedido, arquivo="notificacoes.txt"):
        self.__pedido = pedido
        self.__arquivo = arquivo

    def atualizar(self, mensagem):
        with open(self.__arquivo, "a", encoding="utf-8") as log:
            log.write(f"Pedido {self.__pedido.numero}: {mensagem}\n")

# PEDIDO
class Pedido:
    def __init__(self, numero, cliente, produtos, endereco="", observacoes=""):
        self.__numero = numero
        self.__cliente = cliente
        self.__produtos = list(produtos)
        self.__endereco = endereco
        self.__observacoes = observacoes
        self.__confirmado = False
        self.__observadores = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def produtos(self):
        return list(self.__produtos)

    @property
    def endereco(self):
        return self.__endereco

    @property
    def observacoes(self):
        return self.__observacoes

    @property
    def confirmado(self):
        return self.__confirmado

    def total(self):
        return sum(produto.preco for produto in self.__produtos)

    def confirmar(self):
        if self.__confirmado:
            raise ValueError(f"Pedido {self.__numero} ja foi confirmado")
        self.__confirmado = True

    def adicionar_observer(self, observer: PedidoObserver):
        self.__observadores.append(observer)

    def remover_observer(self, observer: PedidoObserver):
        self.__observadores.remove(observer)

    def notificar(self, mensagem):
        for observer in self.__observadores:
            observer.atualizar(mensagem)

# BUILDER
class PedidoBuilder:
    def __init__(self):
        self.__numero = None
        self.__cliente = None
        self.__produtos = []
        self.__endereco = ""
        self.__observacoes = ""

    def numero(self, valor):
        self.__numero = valor
        return self

    def cliente(self, valor):
        self.__cliente = valor
        return self

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)
        return self

    def endereco(self, valor):
        self.__endereco = valor
        return self

    def observacao(self, valor):
        self.__observacoes = valor
        return self

    def build(self):
        if not all([self.__numero, self.__cliente, self.__produtos]):
            raise ValueError(
                "Numero, cliente e pelo menos um produto sao obrigatorios"
            )
        return Pedido(
            self.__numero,
            self.__cliente,
            self.__produtos,
            self.__endereco,
            self.__observacoes
        )

# PAGAMENTO
class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

# servicos externos
class GatewayPix:
    def transferir(self, quantia):
        print(f"Pix realizado: R$ {quantia:.2f}")
        return True

class GatewayCartao:
    def cobrar_cartao(self, total):
        print(f"Cartão aprovado: R$ {total:.2f}")
        return True

class GatewayBoleto:
    def emitir_boleto(self, valor):
        print(f"Boleto emitido: R$ {valor:.2f}")
        return True

# ADAPTER
class PixAdapter(Pagamento):
    def __init__(self, gateway: GatewayPix):
        self.__gateway = gateway

    def pagar(self, valor):
        return self.__gateway.transferir(valor)

class CartaoAdapter(Pagamento):
    def __init__(self, gateway: GatewayCartao):
        self.__gateway = gateway

    def pagar(self, valor):
        return self.__gateway.cobrar_cartao(valor)

class BoletoAdapter(Pagamento):
    def __init__(self, gateway: GatewayBoleto):
        self.__gateway = gateway

    def pagar(self, valor):
        return self.__gateway.emitir_boleto(valor)

# FINALIZADOR
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

# SISTEMA
def exibir_pedido(pedido, forma_pagamento):
    print("========== LOJA VIRTUAL ==========")
    print(f"Cliente: {pedido.cliente}")
    print(f"Pedido: {pedido.numero}")
    print("Produtos:")
    for produto in pedido.produtos:
        print(f"- {produto.nome}: R$ {produto.preco:.2f}")
    print(f"Total: R$ {pedido.total():.2f}")
    print(f"Forma de pagamento: {forma_pagamento}\n")

def registrar_observers(pedido):
    pedido.adicionar_observer(EmailObserver(pedido))
    pedido.adicionar_observer(EstoqueObserver(pedido))
    pedido.adicionar_observer(FinanceiroObserver(pedido))
    pedido.adicionar_observer(LogObserver(pedido))

teclado = Produto(1, "Teclado Mecânico", 250.00)
mouse = Produto(2, "Mouse Gamer", 150.00)
monitor = Produto(3, "Monitor 24", 900.00)

pedido = (
    PedidoBuilder()
    .numero(1001)
    .cliente("Maria")
    .adicionar_produto(teclado)
    .adicionar_produto(mouse)
    .endereco("Rua das Flores, 100")
    .observacao("Entregar pela manhã")
    .build()
)
registrar_observers(pedido)

exibir_pedido(pedido, "PIX")
FinalizadorPedido(pedido, PixAdapter(GatewayPix())).finalizar()
print("\n========== FINALIZADO ==========\n")

print("--- Tentativa de pagar o mesmo pedido novamente ---")
FinalizadorPedido(pedido, CartaoAdapter(GatewayCartao())).finalizar()

print("\n--- Segundo pedido (Boleto) ---")
pedido2 = (
    PedidoBuilder()
    .numero(1002)
    .cliente("João")
    .adicionar_produto(monitor)
    .build()
)
registrar_observers(pedido2)

exibir_pedido(pedido2, "BOLETO")
FinalizadorPedido(pedido2, BoletoAdapter(GatewayBoleto())).finalizar()
print("\n========== FINALIZADO ==========")
