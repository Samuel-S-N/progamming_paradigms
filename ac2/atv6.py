class Publicacao:
    
    def __init__(self, titulo, ano):
        self.__titulo = titulo
        self.__ano = ano
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano

class Livro(Publicacao):
    
    def __init__(self,titulo, ano, editora):
        super().__init__(titulo, ano)
        self.editora = Editora(editora)

    def exibir_informacoes(self):
        print("Livro: Programação em python")

class Revista(Publicacao):
    
    def __init__(self,titulo, ano, editora):
        super().__init__(titulo, ano)
        self.editora = Editora(editora)

    def exibir_informacoes(self):
        print("Revista: Tecnologia hoje")

class Editora:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

livros = [
    Livro("Programação em python", 2026, "Editora Saraiva"),
    Revista("Tecnologia hoje", 2026, "Editora Abril")
]

for livro in livros:
    livro.exibir_informacoes()