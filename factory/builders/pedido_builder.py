from models.pedido import Pedido


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
