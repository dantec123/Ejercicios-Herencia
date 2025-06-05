class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def calcular_eficiencia_combustible(self):
        raise NotImplementedError(" debe ser implementado por las subclases")

    def proyectar_combustible_necesario(self, distancia_km):

        eficiencia = self.calcular_eficiencia_combustible()
        if eficiencia <= 0:
            raise ValueError(" debe ser mayor que cero")
        return distancia_km / eficiencia


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, eficiencia_km_l):
        super().__init__(marca, modelo, año)
        self.eficiencia_km_l = eficiencia_km_l  

    def calcular_eficiencia_combustible(self):
        return self.eficiencia_km_l


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, eficiencia_km_l):
        super().__init__(marca, modelo, año)
        self.eficiencia_km_l = eficiencia_km_l  

    def calcular_eficiencia_combustible(self):
        return self.eficiencia_km_l
