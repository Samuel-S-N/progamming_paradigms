class Carro:

    def __init__(self, cor, modelo, ano):
        
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        
    def Mostrar_dados(self):
        
        print("Cor: ",self.cor)
        print("Modelo: ",self.modelo)
        print("Ano: ",self.ano)
        pass
    
    def Ligar_carro(self):
    
        print("O carro está ligado!")
        
c1 = Carro("Azul", "Civic", 2008)
c1.Mostrar_dados()
c1.Ligar_carro()