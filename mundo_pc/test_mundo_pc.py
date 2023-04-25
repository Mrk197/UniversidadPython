from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

monitor1 = Monitor('Huawei', 15)
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)
teclado2 = Teclado('Logitec', "USB")
computadora2 = Computadora('Acer', monitor1, teclado2, raton1)
orden1 = Orden([computadora1, computadora2])
print(orden1)
raton2 = Raton('Aurus', 'Bluetooth')
computadora3 = Computadora('Asus', monitor1, teclado1, raton2)
orden1.agregar_computadora(computadora3)
print(orden1)
