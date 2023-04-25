#POLOMORFISMO: multiples formas en tiempo de ejecución. Una misma variable puede ejecutar metodos diferentes dependiendo
#de la clase a la que apunte.
from POO.Polimorfismo.Empleado import Empleado
from POO.Polimorfismo.Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto) #de manera indirecta manda a llamar método str
    print(type(objeto)) #indica clase del obj
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente): #si el objeto es instancia de Gerente
        print(objeto.departamento) #se imprime le atributo 


empleado = Empleado('Juan', '5000')
imprimir_detalles(empleado)

gerente = Gerente('Karla', '6000', 'Sistemas')
imprimir_detalles(gerente)
