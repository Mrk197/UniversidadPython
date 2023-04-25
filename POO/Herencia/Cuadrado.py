from FiguraGeometrica import FiguraGeometrica
from Color import Color #as NuevoNombre


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #super().__init__() ##No recomendable en herencia multiple
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'Cuadrado -> {FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
    