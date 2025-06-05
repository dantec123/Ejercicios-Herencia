from datetime import date, timedelta

class Producto:
    def __init__(self, nombre, precio, fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_info(self):
        print(f"{self.nombre} - Precio: ${self.precio} - Vence: {self.fecha_vencimiento}")


class ProductoAlimenticio(Producto):
    def aplicar_descuento(self):
        dias_restantes = (self.fecha_vencimiento - date.today()).days
        if (dias_restantes <= 5):
            return self.precio * 0.5
        return self.precio


class ProductoElectronico(Producto):
    def aplicar_descuento(self):
        return self.precio * 0.9  

if __name__ == "__main__":
    p1 = ProductoAlimenticio("Mondongo", 1000, date.today() + timedelta(days=3))
    p2 = ProductoAlimenticio("Milanesa", 120, date.today() + timedelta(days=10))
    p3 = ProductoElectronico("Televisor", 20000, date.today() + timedelta(days=365))

    print("Producto Alimenticio (próximo a vencer):")
    p1.mostrar_info()
    print("Precio con descuento:", p1.aplicar_descuento())

    print("\nProducto Alimenticio (sin descuento):")
    p2.mostrar_info()
    print("Precio con descuento:", p2.aplicar_descuento())

    print("\nProducto Electrónico:")
    p3.mostrar_info()
    print("Precio con descuento:", p3.aplicar_descuento())
