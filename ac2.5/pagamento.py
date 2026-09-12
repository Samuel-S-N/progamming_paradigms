from abc import ABC, abstractmethod


class Pagamento(ABC):

    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar(self):
        pass


class PagamentoPix(Pagamento):

    def processar(self):
        print(f"PIX de R$ {self.valor:.2f} processado.")


class PagamentoCartao(Pagamento):

    def processar(self):
        print(f"Pagamento no cartão de R$ {self.valor:.2f} processado.")


class PagamentoBoleto(Pagamento):

    def processar(self):
        print(f"Boleto de R$ {self.valor:.2f} gerado.")


class PagamentoPayPal(Pagamento):

    def processar(self):
        print(f"Pagamento PayPal de R$ {self.valor:.2f} processado.")


class ComprovanteService:

    def gerar(self, pagamento):
        print(f"Comprovante gerado no valor de R$ {pagamento.valor:.2f}")


class PagamentoRepository:

    def salvar(self, pagamento):
        print(f"Pagamento de R$ {pagamento.valor:.2f} salvo.")


pix = PagamentoPix(100)
cartao = PagamentoCartao(250)
boleto = PagamentoBoleto(500)

pix.processar()
cartao.processar()
boleto.processar()

comprovante = ComprovanteService()
repository = PagamentoRepository()

comprovante.gerar(pix)
repository.salvar(pix)

paypal = PagamentoPayPal(300)
paypal.processar()
comprovante.gerar(paypal)
repository.salvar(paypal)
