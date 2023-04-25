class Producto:
    contador_productos = 0 #VARIABLE DE CLASE

    def __init__(self, nombre, precio): #MÉTODO INICIALIZADOR
        Producto.contador_productos += 1
        #PROPIEDADES ABSTRACTAS
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    #MÉTODOS GET Y SET DE LAS PROPIEDADES ABSTRACTAS
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self): #MÉTODO DE IMPRESIÓN
        return f'Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'


if __name__ == '__main__':  #PARA HACER PRUEBAS DE MANERA INTERNA
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalón', 150.00)
    print(producto2)