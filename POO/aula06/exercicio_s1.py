class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
class calcularSalario:
        def calcular(self, funcionario):
            print(f"Calculando o salário do funcionário {funcionario.nome} no banco.")

class SalvarBanco:

    def salvarBanco(self):
        print(f"Salvando o funcionario {self.nome}")

class EnviarEmail:

    def enviar(self, funcionario):
        print(f"enviando email para {funcionario.nome}")

funcionario = Funcionario("Erik", 500)
salario = calcularSalario()
bd = SalvarBanco()
email = EnviarEmail()