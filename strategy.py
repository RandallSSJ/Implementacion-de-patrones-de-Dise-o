class PagoEfectivo:
    def pagar(self, monto):
        print(f"Pagando en efectivo: {monto}")

class PagoTarjeta:
    def pagar(self, monto):
        print(f"Pagando con tarjeta: {monto}")

class Pago:
    def _init_(self, metodo):
        self.metodo = metodo

    def procesar(self, monto):
        self.metodo.pagar(monto)