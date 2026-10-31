from builders.pedido_builder import PedidoBuilder
from models.produto import Produto
from observers.email_observer import EmailObserver
from observers.estoque_observer import EstoqueObserver
from observers.financeiro_observer import FinanceiroObserver
from observers.log_observer import LogObserver
from pagamentos.boleto_adapter import BoletoAdapter
from pagamentos.cartao_adapter import CartaoAdapter
from pagamentos.gateway_boleto import GatewayBoleto
from pagamentos.gateway_cartao import GatewayCartao
from pagamentos.gateway_pix import GatewayPix
from pagamentos.pix_adapter import PixAdapter
from services.finalizador_pedido import FinalizadorPedido


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
