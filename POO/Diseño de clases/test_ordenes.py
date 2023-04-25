from Orden import Orden
from Producto import  Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalón', 150.00)
producto3 = Producto('Falda', 120.00)
producto4 = Producto('Blusa', 70.00)

productos = [producto1, producto2]
orden1 = Orden(productos)
print(orden1)
print(f'Total: {orden1.calcular_total()}')
print('\n')
productos2 = [producto3, producto4]
orden2 = Orden(productos2)
orden2.agregar_producto(producto1)
print(orden2)
print(f'Total: {orden2.calcular_total()}')
