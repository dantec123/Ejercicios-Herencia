class Pago:
    def __init__(self, monto, fecha):
        self.monto = monto
        self.fecha = fecha

    def mostrar_detalles(self):
        print(f"Monto: ${self.monto}, Fecha: {self.fecha}")

    def procesar_pago(self):
        print("Procesando pago genérico.")


class PagoTarjeta(Pago):
    def procesar_pago(self):
        print(f"Procesando pago con tarjeta por ${self.monto}.")


    def generar_recibo(self):
        print(f"Recibo: Pago con tarjeta de ${self.monto} en fecha {self.fecha}.")


class PagoPayPal(Pago):
    def procesar_pago(self):
        print(f"Procesando pago con PayPal por ${self.monto}.")


    def generar_recibo(self):
        print(f"Recibo: Pago con PayPal de ${self.monto} en fecha {self.fecha}.")


if __name__ == "__main__":
    pago1 = PagoTarjeta(2000, "2025-10-10")
    pago2 = PagoPayPal(3500, "2025-10-10")

    pago1.mostrar_detalles()
    pago1.procesar_pago()
    pago1.generar_recibo()



    pago2.mostrar_detalles()
    pago2.procesar_pago()
    pago2.generar_recibo()
