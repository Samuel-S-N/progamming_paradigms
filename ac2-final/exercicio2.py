from abc import ABC, abstractmethod

# o problema original: CalculadoraFrete decide o valor do frete com if/elif por tipo,
# então toda vez que surge uma modalidade nova preciso alterar essa classe, violando o OCP.
# a solução é criar uma classe abstrata Frete e uma subclasse por modalidade,
# assim novas modalidades só exigem uma classe nova, sem tocar nas existentes.
class Frete(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass


class FreteNormal(Frete):
    def calcular(self, valor):
        return valor * 0.05


class FreteExpresso(Frete):
    def calcular(self, valor):
        return valor * 0.10


class FreteSedex(Frete):
    def calcular(self, valor):
        return valor * 0.15


class FreteInternacional(Frete):
    def calcular(self, valor):
        return valor * 0.20


def calcular_frete(frete, valor):
    return frete.calcular(valor)


if __name__ == "__main__":
    frete = FreteExpresso()
    valor_frete = calcular_frete(frete, 1000)
    print(valor_frete)

    print(calcular_frete(FreteNormal(), 1000))
    print(calcular_frete(FreteSedex(), 1000))
    print(calcular_frete(FreteInternacional(), 1000))
