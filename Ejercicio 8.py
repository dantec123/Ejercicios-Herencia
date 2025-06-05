class Transporte:
    def __init__(self, capacidad, velocidad_maxima):
        self.capacidad = capacidad
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"Capacidad: {self.capacidad}, Velocidad máxima: {self.velocidad_maxima} km/h")


class Avion(Transporte):
    def calcular_tiempo(self, distancia):
        return distancia / self.velocidad_maxima


class Barco(Transporte):
    def calcular_tiempo(self, distancia):
        return distancia / self.velocidad_maxima


if __name__ == "__main__":
    avion = Avion(220, 970)
    barco = Barco(510, 130)

    distancia = 1650  

    print("Avión:")
    avion.mostrar_info()
    print(f"Tiempo estimado para recorrer {distancia} km: {avion.calcular_tiempo(distancia)} horas")

    print("\nBarco:")
    barco.mostrar_info()
    print(f"Tiempo estimado para recorrer {distancia} km: {barco.calcular_tiempo(distancia)} horas")

