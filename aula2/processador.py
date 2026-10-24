from pedido import Pedido
from factories.comprovante_creator import ComprovanteCreator


class ProcessadorPedido:
    def __init__(self, pedido: Pedido, creator: ComprovanteCreator):
        self._pedido = pedido
        self._creator = creator

    def processar(self):
        total = self._pedido.calcular_total_final()
        self._creator.emitir_comprovante(self._pedido, total)
        return total
