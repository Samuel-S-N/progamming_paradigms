class CursoOnline:
    
    def __init__(self, titulo, cargaHoraria):
        self.__titulo = titulo
        self.__cargaHoraria = cargaHoraria
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

class CursoProgramacao(CursoOnline):
    
    def __init__(self,titulo, cargaHoraria, instrutor):
        super().__init__(titulo, cargaHoraria)
        self.instrutor = Instrutor(instrutor)

    def iniciarAula(self):
        print("Iniciando aula de programação.")

class CursoDesign(CursoOnline):
    
    def __init__(self,titulo, cargaHoraria, instrutor):
        super().__init__(titulo, cargaHoraria)
        self.instrutor = Instrutor(instrutor)

    def iniciarAula(self):
        print("Iniciando aula de design.")

class Instrutor:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
cursos = [
    CursoProgramacao("Curso de Python", 100, "João"),
    CursoDesign("Curso de Design", 50, "Maria")
]

for curso in cursos:
    curso.iniciarAula()