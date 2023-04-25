from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica

#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

print('Creación Objeto Cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
cuadrado1.alto = 11 #si es un valor no valido se deja el valor que tenía
print(cuadrado1.color)
print(cuadrado1.calcular_area())
print(cuadrado1)

print('Creación Objeto Rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(base=14, altura=5, color='Azul')
print(rectangulo1.area())
print(rectangulo1)
#MRO - Method Resolution Order
#print(Cuadrado.mro())
