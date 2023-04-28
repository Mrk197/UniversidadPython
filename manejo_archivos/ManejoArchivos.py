#CONTEXT MANAGER

class ManejoArchivos: #o recursos

    def __init__(self, nombre): #s recib nombre del recurso
        self.nombre = nombre

    def __enter__(self): #definidos en la calse object (padre)
        print('obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, exc_type, exc_val, exc_traza): #debe llevar todos los parámetros aunque no se ues
        print('Cerramos el recurso'.center(50, '-'))
        if self.nombre: #esta apuntando a algún objeto? (esta abierto el recurso)
            self.nombre.close()
