from Producto import Producto

class Orden:

    cont_orden = 0

    def __init__(self, productos): #va a recibir una lista de productos
        Orden.cont_orden += 1
        self._id_orden = Orden.cont_orden
        self._productos = list(productos) #se hace conversión a lista para seciorarse que se recibio una lista (arroja error si no)

    def agregar_producto(self, producto):
        self._productos.append(producto) #se agrega al final de la lista

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += '\n|' + producto.__str__()

        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'


if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalón', 150.00)
    productos = [producto1, producto2]
    orden1 = Orden(productos)
    print(orden1)
