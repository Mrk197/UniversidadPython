class Persona:
    #agregar caracteristicas o atributos
    mi_atributo = '' #atributos de clase
    def __init__(self, nombre, apellido, edad): #método similar a un constructor (tipo dunder)
        #atributos de instancia
        self._nombre = nombre  # _ indica que atrbuto es encapsulado(sólo se accede de manera local)
        self.__apellido = apellido # __ restringe más el acceso
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self.__apellido} {self.edad}')

    #Métdos GET y SET
    @property  #decorador, modifica metodo como si fuera un atributo de la clase (sin hacer persona.nombre())
    def nombre(self):
        return self._nombre
    #sin el método SET se cncierte en sólo lectura
    @nombre.setter #poder usar método para modificar nombre como si fuera una propiedad
    def nombre(self, nombre):
        self._nombre = nombre

    #Método Destructor
    def __del__(self):
        print(f'Persona: {self._nombre} {self.__apellido}')


if __name__ == '__main__':  #el siguente código sólo se ejecuta si se esta haciendo la ejecución desde el archivo main (este archivo)
    persona1 = Persona('Jan',  'Gomez', '28')
    print(persona1._nombre)
    persona1.__apellido = 'Perez'
    persona1.mostrarDetalle()
    persona1.telefono = '5611178364' #atributo solo estara disponible para este objeto
    print(persona1.telefono)

    persona2 = Persona('Karla', 'Gomez', 30)
    print(persona2._nombre)
    # persona2.mostrarDetalle()
    Persona.mostrarDetalle(persona2) #otra forma de llamar el método


    #Modificar atributos
    persona1._nombre = 'Juan Carlos'
    print(persona1._nombre, persona1.__apellido)
    persona1.mostrarDetalle()


    #ENCAPSULAMIENTO
    print("ENCAPSULAMIENTO ")
    print(persona1.nombre) #se accede de esta manera debido a property
    persona1.nombre = "Jan Carlos"
    print(persona1.nombre)

    print(__name__)