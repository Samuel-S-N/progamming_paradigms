from abc import ABC, abstractmethod

class Computador:
    def __init__(
        self,
        processador,
        memoria,
        armazenamento,
        placa_video=None
    ):

        self.processador = processador
        self.memoria = memoria
        self.armazenamento = armazenamento
        self.placa_video = placa_video
    
    def exibir(self):
        print(f"processador: {self.processador}")
        print(f"memoria: {self.memoria}")
        print(f"armazenamento: {self.armazenamento}")
        print(f"placa_video: {self.placa_video}")

class ComputadorBuilder:
    def __init__(self):
        self.__processador = None
        self.__memoria = None
        self.__armazenamento = None
        self.__placa_video = None

    def processador (self, valor):
        self.__processador = valor
        return self

    def memoria(self, valor):
        self.__memoria = valor
        return self
    
    def armazenamento (self, valor):
        self.__armazenamento = valor
        return self

    def placa_video(self, valor):
        self.__placa_video = valor
        return self
    
    def build(self):
        if not all([
            self.__processador,
            self.__memoria,
            self.__armazenamento
        ]):
            raise ValueError(
            "Processador, memoria e armazenamento são obrigatorios"
        )
        return Computador(
            self.__processador,
            self.__memoria,
            self.__armazenamento,
            self.__placa_video
        )

#SITEMA
computador = (
    ComputadorBuilder()
    .processador("Ryzen 7")
    .memoria("32GB")
    .armazenamento("1TB SSD")
    .placa_video("RTX 4060")
    .build()
)

computador.exibir()
