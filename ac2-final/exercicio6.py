from abc import ABC, abstractmethod

# o problema: Pinguim herda de Ave e é obrigado a sobrescrever voar(), mas como pinguim não voa,
# o método só lança uma exceção. isso viola o LSP: em qualquer lugar que espera uma Ave e chama
# voar(), substituir por um Pinguim quebra o programa em vez de manter o comportamento esperado.
# a solução separa aves que voam de aves que não voam em hierarquias diferentes, então cada
# classe só promete o comportamento que realmente consegue cumprir.
class Ave(ABC):
    pass


class AveVoadora(Ave):
    @abstractmethod
    def voar(self):
        pass


class AveNaoVoadora(Ave):
    @abstractmethod
    def andar(self):
        pass


class Aguia(AveVoadora):
    def voar(self):
        print("A águia está voando.")


class Pardal(AveVoadora):
    def voar(self):
        print("O pardal está voando.")


class Pinguim(AveNaoVoadora):
    def andar(self):
        print("O pinguim está andando.")


if __name__ == "__main__":
    aves_voadoras = [Aguia(), Pardal()]
    for ave in aves_voadoras:
        ave.voar()

    pinguim = Pinguim()
    pinguim.andar()
