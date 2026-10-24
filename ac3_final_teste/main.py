from abc import ABC, abstractmethod


class Produto:
    def __init__(self, nome, preco, quantidade):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def get_quantidade(self):
        return self._quantidade

    def calcular_subtotal(self):
        return self._preco * self._quantidade

class DescontoStrategy(ABC):
    @abstractmethod
    def calcular(self, valor):
        """Retorna o valor do desconto a ser aplicado sobre `valor`."""


class DescontoComum(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.05


class DescontoVIP(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.10


class DescontoPremium(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.20


class Pedido:
    def __init__(self, desconto: DescontoStrategy):
        self._produtos = []
        self._desconto = desconto

    def adicionar_produto(self, produto: Produto):
        self._produtos.append(produto)

    def get_produtos(self):
        return list(self._produtos)

    def calcular_total_bruto(self):
        return sum(p.calcular_subtotal() for p in self._produtos)

    def calcular_desconto(self):
        return self._desconto.calcular(self.calcular_total_bruto())

    def calcular_total_final(self):
        return self.calcular_total_bruto() - self.calcular_desconto()

class Comprovante(ABC):
    @abstractmethod
    def emitir(self, pedido: Pedido, total):
        pass

class ComprovanteSimples(Comprovante):
    def emitir(self, pedido, total):
        print(f"Comprovante simples - Total pago: R${total:.2f}")

class ComprovanteDetalhado(Comprovante):
    def emitir(self, pedido, total):
        print("Comprovante detalhado")
        for p in pedido.get_produtos():
            print(f"  {p.get_nome()}: {p.get_quantidade()} x R${p.get_preco():.2f}"
                  f" = R${p.calcular_subtotal():.2f}")
        print(f"  Total bruto: R${pedido.calcular_total_bruto():.2f}")
        print(f"  Desconto:    R${pedido.calcular_desconto():.2f}")
        print(f"  Total final: R${total:.2f}")


class ComprovanteCreator(ABC):
    @abstractmethod
    def criar_comprovante(self) -> Comprovante:
        pass

    def emitir_comprovante(self, pedido, total):
        comprovante = self.criar_comprovante()
        comprovante.emitir(pedido, total)


class ComprovanteSimplesCreator(ComprovanteCreator):
    def criar_comprovante(self) -> Comprovante:
        return ComprovanteSimples()


class ComprovanteDetalhadoCreator(ComprovanteCreator):
    def criar_comprovante(self) -> Comprovante:
        return ComprovanteDetalhado()

class ProcessadorPedido:
    def __init__(self, pedido: Pedido, creator: ComprovanteCreator):
        self._pedido = pedido
        self._creator = creator

    def processar(self):
        total = self._pedido.calcular_total_final()
        self._creator.emitir_comprovante(self._pedido, total)
        return total

class DescontoEspecial(DescontoStrategy):
    def calcular(self, valor):
        return valor * 0.15

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
    print(f"\nDesconto {nome}")
    pedido = Pedido(desconto)
    for produto in produtos:
        pedido.adicionar_produto(produto)

    ProcessadorPedido(pedido, ComprovanteSimplesCreator()).processar()
    ProcessadorPedido(pedido, ComprovanteDetalhadoCreator()).processar()
