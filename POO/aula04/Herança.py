import re


class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    @property
    def idade(self):
        return(self.__idade)
    
    @property
    def nome(self):
        return(self.__nome)

    @property
    def email(self):
        return(self.__email)

    def apresentar(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"email: {self.email}")


class Aluno (Pessoa):
    def __init__(self, nome, idade, email, curso):
        super().__init__(nome, idade, email)
        self.curso = curso

    def apresentar(self):
        super().apresentar()
        print(f"Curso: {self.curso}")       
        
        

aluno1 = Aluno("nome", 18, "email", "CDC")
aluno1.apresentar()