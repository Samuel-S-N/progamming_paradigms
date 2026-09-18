from abc import ABC, abstractmethod

# o problema original: Funcionario guarda o cargo como string e decide o bônus com if/elif
# (viola o OCP, cada cargo novo exige mexer na classe) e ainda acumularia responsabilidades
# de salvar e gerar relatório se essas features fossem coladas nela (violaria o SRP).
# a solução cria uma subclasse de Funcionario para cada cargo, cada uma sabendo calcular
# o próprio bônus, e classes separadas para persistência e relatório.
class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20


class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05


class Analista(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15


class FuncionarioRepository:
    def salvar(self, funcionario):
        print(f"Salvando funcionário {funcionario.nome} no banco de dados...")


class RelatorioService:
    def gerar_relatorio(self, funcionarios):
        for funcionario in funcionarios:
            nome_cargo = funcionario.__class__.__name__
            print(f"{funcionario.nome} ({nome_cargo}): bônus de R$ {funcionario.calcular_bonus():.2f}")


if __name__ == "__main__":
    funcionarios = [
        Desenvolvedor("Carlos", 5000),
        Gerente("Maria", 8000),
        Estagiario("João", 2000),
        Analista("Ana", 6000),
    ]

    for funcionario in funcionarios:
        print(funcionario.calcular_bonus())

    repository = FuncionarioRepository()
    for funcionario in funcionarios:
        repository.salvar(funcionario)

    relatorio = RelatorioService()
    relatorio.gerar_relatorio(funcionarios)
