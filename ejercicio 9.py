class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = {}

    def mostrar_info(self):
        print(f"Tienda: {self.nombre}")
        print(f"Inventario: {self.inventario}")

    def agregar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

    def eliminar_producto(self, producto):
        if producto in self.inventario:
            del self.inventario[producto]

    def calcular_ventas(self, ventas):
        total = 0
        for producto, monto in ventas.items():
            total += monto
        return total


class TiendaRopa(Tienda):
    pass  


class TiendaElectronica(Tienda):
    pass  


if __name__ == "__main__":
    tienda_ropa = TiendaRopa("Ropa Linda")
    tienda_ropa.agregar_producto("Pantalon", 12)
    tienda_ropa.agregar_producto("Remera", 7)
    tienda_ropa.mostrar_info()

    ventas_ropa = {"Pantalon": 10000, "Remera": 5000}
    print("Ventas Totales Tienda Ropa:", tienda_ropa.calcular_ventas(ventas_ropa))



    tienda_elec = TiendaElectronica("Tienda")
    tienda_elec.agregar_producto("Mouse", 5)
    tienda_elec.agregar_producto("Teclado", 20)
    tienda_elec.mostrar_info()

    ventas_elec = {"Mouse": 2000, "Teclado": 3000}
    print("Ventas Totales Tienda Electrónica:", tienda_elec.calcular_ventas(ventas_elec))
