class Pessoa:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    
    @property
    def nome(self):
        return(self.__nome)

    @property
    def email(self):
        return(self.__email)

    def apresentar(self):
        print(f"\nnome: {self.nome}")
        print(f"email: {self.email}")


class Aluno (Pessoa):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.curso = curso

    def apresentar(self):
        super().apresentar()
        print(f"Curso: {self.curso}\n")  

class Professor (Pessoa):
    
    def __init__(self, nome, email, disciplina):
        super().__init__(nome, email)
        self.disciplina = disciplina
    
    def apresentar(self):
        super().apresentar()
        print(f"Disciplina: {self.disciplina}\n")

class Biblioteca():

    def __init__(self, livro):
        self.__livro = livro

    @property
    def livro(self):
        return(self.__livro)

    def apresentar(self):
        self.livro.apresentar()


class Livro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor

    @property
    def titulo(self):
        return(self.__titulo)
    
    @property
    def autor(self):
        return(self.__autor)

    def apresentar(self):
        print(f"\nTitulo: {self.titulo}")
        print(f"Autor: {self.autor}\n")

aluno1 = Aluno("Samuel", "samuel@email.com", "CDC")
aluno1.apresentar()

professor1 = Professor("Erik", "Erik@email.com", "POO")
professor1.apresentar()

livro1 = Livro("Matador", "George")
biblioteca1 = Biblioteca(livro1)
biblioteca1.apresentar()
