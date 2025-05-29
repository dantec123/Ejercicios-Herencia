class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def emitir_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def mostrar_detalles(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def emitir_sonido(self):
        return "Guau"

    def mostrar_detalles(self):
        detalles = super().mostrar_detalles()
        return f"{detalles}, Raza: {self.raza}"


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def emitir_sonido(self):
        return "Miau"

    def mostrar_detalles(self):
        detalles = super().mostrar_detalles()
        return f"{detalles}, Color: {self.color}"   
