class GatewayBoleto:
    def emitir_boleto(self, valor):
        print(f"Boleto emitido: R$ {valor:.2f}")
        return True
