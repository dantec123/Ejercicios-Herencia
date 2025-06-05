class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"{self.marca} {self.modelo} ({self.año})")


class Automovil(Vehiculo):
    def eficiencia_combustible(self):
        return 15  

    def proyectar_combustible(self, distancia):
        return distancia / self.eficiencia_combustible()


class Motocicleta(Vehiculo):
    def eficiencia_combustible(self):
        return 30  

    def proyectar_combustible(self, distancia):
        return distancia / self.eficiencia_combustible()


if __name__ == "__main__":
    auto = Automovil("Ford", "Fiesta", 2012)
    moto = Motocicleta("Kawasaki", "Z900", 2017)

    distancia = 300  

    print("Automóvil:")
    auto.mostrar_info()
    print(f"Eficiencia: {auto.eficiencia_combustible()} km/l")
    print(f"Combustible necesario para {distancia} km: {auto.proyectar_combustible(distancia)} litros")

    print("\nMotocicleta:")
    moto.mostrar_info()
    print(f"Eficiencia: {moto.eficiencia_combustible()} km/l")
    print(f"Combustible necesario para {distancia} km: {moto.proyectar_combustible(distancia)} litros")
