from factories.comprovante import Comprovante


class ComprovanteSimples(Comprovante):
    def emitir(self, pedido, total):
        print(f"Comprovante simples - Total pago: R${total:.2f}")


class ComprovanteDetalhado(Comprovante):
    def emitir(self, pedido, total):
        print("Comprovante detalhado")
        for p in pedido.get_produtos():
            print(f"  {p.get_nome()}: {p.get_quantidade()} x R${p.get_preco():.2f}"
                  f" = R${p.calcular_subtotal():.2f}")
        print(f"  Total bruto: R${pedido.calcular_total_bruto():.2f}")
        print(f"  Desconto:    R${pedido.calcular_desconto():.2f}")
        print(f"  Total final: R${total:.2f}")
