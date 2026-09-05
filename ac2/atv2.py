class Produto:
    
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco

class ProdutoFisico(Produto):
    
    def __init__(self,nome, preco, fornecedor):
        super().__init__(nome, preco)
        self.fornecedor = Fornecedor(fornecedor)

    def entregar(self):
        print("O produto fisico será entregue pelo Correios.")

class ProdutoDigital(Produto):
    
    def __init__(self,nome, preco, fornecedor):
        super().__init__(nome, preco)
        self.fornecedor = Fornecedor(fornecedor)

    def entregar(self):
        print("O produto será disponibilizado para download.")

class Fornecedor:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

Produtos = [
    ProdutoFisico("NitroFade", "800", "Puma"),
    ProdutoDigital("GTA VI", "550", "Rockstar")
]

for produto in Produtos:
    produto.entregar()