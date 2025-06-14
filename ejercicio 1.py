import math

class Figura:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def imprimir_detalles(self):
        print(f"Figura: {self.nombre}")
        print(f"Color: {self.color}")

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__("Círculo", color)
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Radio: {self.radio}")
        print(f"Área: {self.calcular_area():.2f}")
        print(f"Perímetro: {self.calcular_perimetro():.2f}")




class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__("Rectángulo", color)
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.calcular_area():.2f}")
        print(f"Perímetro: {self.calcular_perimetro():.2f}")

# Ejemplo de uso:
if __name__ == "__main__":
    c = Circulo("Rojo", 5)
    c.imprimir_detalles()
    print()  # Línea en blanco para separar

    r = Rectangulo("Azul", 4, 7)
    r.imprimir_detalles()

