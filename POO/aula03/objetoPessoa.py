class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Samuel", 23)
p2 = Pessoa("Maria", 20)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

print(f"{p1.nome, p1.idade}\n{p2.nome, p2.idade}")