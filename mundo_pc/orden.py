from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Orden:

    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self.computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        orden = f'id: {self._id_orden} \n'
        for computador in self.computadoras:
            orden += f'{computador} \n'

        return orden


if __name__ == '__main__':
    monitor1 = Monitor('Huawei', 15)
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    computadora2 = Computadora('Acer', monitor1, teclado1, raton1)
    orden1 = Orden([computadora2,computadora1])
    print(orden1)
    computadora3 = Computadora('Asus', monitor1, teclado1, raton1)
    orden1.agregar_computadora(computadora3)
    print(orden1)
