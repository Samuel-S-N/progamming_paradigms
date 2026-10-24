from produto import Produto
from pedido import Pedido
from processador import ProcessadorPedido
from strategies.descontos_concretos import (
    DescontoComum, DescontoVIP, DescontoPremium, DescontoEspecial,
)
from factories.comprovante_creator import (
    ComprovanteSimplesCreator, ComprovanteDetalhadoCreator,
)

produtos = [
    Produto("Notebook", 3500.00, 1),
    Produto("Mouse", 80.00, 2),
    Produto("Teclado", 150.00, 1),
]

descontos = [
    ("Comum (5%)", DescontoComum()),
    ("VIP (10%)", DescontoVIP()),
    ("Premium (20%)", DescontoPremium()),
    ("Especial (15%)", DescontoEspecial()),
]

for nome, desconto in descontos:
    print(f"\n=== Desconto {nome} ===")
    pedido = Pedido(desconto)
    for produto in produtos:
        pedido.adicionar_produto(produto)

    ProcessadorPedido(pedido, ComprovanteSimplesCreator()).processar()
    ProcessadorPedido(pedido, ComprovanteDetalhadoCreator()).processar()

print("\n=== Validação ===")
for args in [("Defeito", -1, 1), ("Defeito", 10, 0)]:
    try:
        Produto(*args)
    except ValueError as e:
        print(f"Erro: {e}")
