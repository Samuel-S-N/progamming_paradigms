class Aluno:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

class CalcularMedia:
    
    def calcular(self, aluno):
        print(f"A media do aluno {aluno.nome} é {aluno.nota}")

class AlunoRepository:
    
    def salvar(self, aluno):
        print(f"Salvando {aluno.nome}")

class EmailService:

    def enviar(self, aluno):
        print(f"Enviando email para {aluno.nome}")

aluno = Aluno("Samuel", 8.0)

media = CalcularMedia()
bd = AlunoRepository()
email = EmailService()

#print(media.calcular(aluno))
media.calcular(aluno)
bd.salvar(aluno)
email.enviar(aluno)

