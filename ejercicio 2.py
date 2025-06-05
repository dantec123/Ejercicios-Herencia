class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Cargo: {self.cargo}, Salario: {self.salario}")


class Gerente(Empleado):
    def calcular_aumento(self):
        return self.salario * 1.20


class EmpleadoTemporal(Empleado):
    def calcular_aumento(self):
        return self.salario * 1.05


if __name__ == "__main__":
    g = Gerente("Pedro", 5698, "Gerente")
    et = EmpleadoTemporal("Juan", 2500, "Temporal")

    g.mostrar_info()
    print("Nuevo salario Gerente:", g.calcular_aumento())



    et.mostrar_info()
    print("Nuevo salario Empleado Temporal:", et.calcular_aumento())
