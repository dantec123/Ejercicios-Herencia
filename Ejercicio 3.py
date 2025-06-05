class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_detalles(self):
        print(f"Nombre del animal: {self.nombre}")

    def emitir_sonido(self):
        print("")


class Perro(Animal):
    def emitir_sonido(self):
        print("Guau!")


class Gato(Animal):
    def emitir_sonido(self):
        print("Miau!")


if __name__ == "__main__":
    perro = Perro("perro1")
    gato = Gato("gato1")

    print("Perro:")
    perro.mostrar_detalles()
    perro.emitir_sonido()

    print("\nGato:")
    gato.mostrar_detalles()
    gato.emitir_sonido()
