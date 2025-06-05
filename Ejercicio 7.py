class Instrumento:
    def __init__(self, nombre, material):
        self.nombre = nombre
        self.material = material

    def tipo_sonido(self):
        print(f"El instrumento {self.nombre} produce un sonido acústico.")


class Guitarra(Instrumento):
    def tocar_nota(self):
        print(f"La guitarra {self.nombre} toca la nota: Do.")


class Piano(Instrumento):
    def tocar_nota(self):
        print(f"El piano {self.nombre} toca la nota: Re.")


if __name__ == "__main__":
    guitarra = Guitarra("Guitarra acustica", "Madera")
    piano = Piano("Piano Yamaha", "Madera")

    guitarra.tipo_sonido()
    guitarra.tocar_nota()

    piano.tipo_sonido()
    piano.tocar_nota()
