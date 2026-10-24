from abc import ABC, abstractmethod


class Material(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    @abstractmethod
    def disponibilizar(self):
        pass


class Livro(Material):
    def disponibilizar(self):
        print(f"Livro: {self.titulo} emprestado.")


class Revista(Material):
    def disponibilizar(self):
        print(f"Revista: {self.titulo} emprestada.")


class Ebook(Material):
    def disponibilizar(self):
        print(f"Ebook: {self.titulo} liberado.")


class Devolvivel(ABC):
    @abstractmethod
    def devolver(self):
        pass


class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass


livro = Livro("Python para Iniciantes", "Vieira")
revista = Revista("Tecnologia Hoje", "Samuel")
ebook = Ebook("Aprendendo POO", "Pedro")

livro.disponibilizar()
revista.disponibilizar()
ebook.disponibilizar()