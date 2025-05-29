class Empleado:
    def __init__(self, nombre, salario, cargo):
        self.nombre = nombre
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}, Cargo: {self.cargo}"

    def calcular_aumento(self):

        raise NotImplementedError("Debe implementarse en las subclases.")


class Gerente(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario, "Gerente")

    def calcular_aumento(self):
   
        if self.salario < 1000:
            aumento = self.salario * 0.15
        else:
            aumento = self.salario * 0.10
        return self.salario + aumento


class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, salario, meses_contratado):
        super().__init__(nombre, salario, "Empleado Temporal")
        self.meses_contratado = meses_contratado

    def calcular_aumento(self):
    
        if self.meses_contratado > 4:
            aumento = self.salario * 0.06
        else:
            aumento = self.salario * 0.03
        return self.salario + aumento
