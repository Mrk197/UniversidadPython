from mundo_pc.monitor import Monitor


class Computadora:

    contados_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton): #(string, ref a obj, ref a obj, ref a obj)
        Computadora.contados_computadoras += 1
        self._id_computadoras = Computadora.contados_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
            {self._nombre}:{self._id_computadoras}
            Nombre: {self._nombre} 
            Monitor: {self._monitor}
            Teclado: {self._teclado} 
            Ratón: {self._raton}
            '''

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton


if __name__ == "__main__":
    monitor1 = Monitor('Huawei', 15)
    computadora1 = Computadora('HP', monitor1, 'HP', 'HP')
    print(computadora1)

    computadora2 = Computadora('Acer', monitor1, 'HP', 'HP')
    print(computadora2)

