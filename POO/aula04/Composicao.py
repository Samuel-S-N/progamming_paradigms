class Motor:

        def ligar(self):
            print("motor ligado")
        

class Carro:

    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor()

    def ligar(self):
        print(f"Ligando {self.modelo}")
        self.motor.ligar()

carro = Carro("Fusca")
carro.ligar()