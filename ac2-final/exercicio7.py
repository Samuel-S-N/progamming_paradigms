from abc import ABC, abstractmethod

# o problema: ContaInvestimento herda de Conta e é forçada a sobrescrever sacar() só para lançar
# uma exceção, porque a classe pai promete um comportamento (sacar) que ela não pode cumprir.
# isso viola o LSP: qualquer código que use realizar_saque(conta, valor) esperando uma Conta
# quebra ao receber uma ContaInvestimento. ou seja, ContaInvestimento não deveria herdar de uma
# classe que promete sacar().
# a solução tira a "promessa" de saque da classe base e coloca numa abstração própria
# (ContaSacavel), que só as contas que realmente permitem saque implementam. ContaInvestimento
# nunca herda dessa promessa, então nunca finge suportar um comportamento que não tem — sem
# precisar checar o tipo do objeto com if/type()/isinstance() em nenhum lugar.
class Conta(ABC):
    def __init__(self, saldo):
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass


class ContaSacavel(ABC):
    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta, ContaSacavel):
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


class ContaInvestimento(Conta):
    def depositar(self, valor):
        self.saldo += valor


def realizar_saque(conta: ContaSacavel, valor):
    conta.sacar(valor)
    print("Saque realizado!")


if __name__ == "__main__":
    conta_corrente = ContaCorrente(1000)
    realizar_saque(conta_corrente, 200)
    print(conta_corrente.saldo)

    conta_investimento = ContaInvestimento(1000)
    conta_investimento.depositar(500)
    print(conta_investimento.saldo)

    # conta_investimento não tem sacar(), então nem é compatível com realizar_saque:
    # realizar_saque(conta_investimento, 200) geraria AttributeError — a própria ausência
    # do método já impede o uso indevido, sem precisar de isinstance/type() em lugar nenhum.
