from abc import ABC, abstractmethod

# o problema original: Pagamento decide a forma de pagamento com if/elif (viola o OCP, toda forma
# nova exige mexer na classe) e ainda acumula responsabilidades de salvar no banco e enviar
# comprovante dentro do mesmo método (viola o SRP).
# a solução separa cada forma de pagamento em uma subclasse com processar(valor), e move
# persistência e comprovante para classes próprias.
class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass


class Pix(Pagamento):
    def processar(self, valor):
        print(f"PIX de R$ {valor}")


class Cartao(Pagamento):
    def processar(self, valor):
        print(f"Cartão de R$ {valor}")


class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Boleto de R$ {valor}")


class Criptomoeda(Pagamento):
    def processar(self, valor):
        print(f"Criptomoeda de R$ {valor}")


class PagamentoRepository:
    def salvar(self, valor):
        print("Salvando pagamento no banco...")


class ComprovanteService:
    def enviar(self, valor):
        print("Enviando comprovante por e-mail...")


if __name__ == "__main__":
    pagamentos = [
        Pix(),
        Cartao(),
        Boleto(),
        Criptomoeda(),
    ]

    repository = PagamentoRepository()
    comprovante = ComprovanteService()

    for pagamento in pagamentos:
        pagamento.processar(500)
        repository.salvar(500)
        comprovante.enviar(500)
