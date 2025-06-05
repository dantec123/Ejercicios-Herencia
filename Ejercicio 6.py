class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera=None):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def asignar_carrera(self, carrera):
        self.carrera = carrera

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Rol: Estudiante, Carrera: {self.carrera}")


class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura=None):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def asignar_asignatura(self, asignatura):
        self.asignatura = asignatura

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Rol: Profesor, Asignatura: {self.asignatura}")


if __name__ == "__main__":
    estudiante = Estudiante("Dante", 18)
    profesor = Profesor("Jorge", 45)

    estudiante.asignar_carrera("Analista de sistemas")
    profesor.asignar_asignatura("Matemáticas")

    estudiante.mostrar_info()

    profesor.mostrar_info()
