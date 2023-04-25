from Persona import Persona

print('Creacion de obejetos '.center(50, '-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrarDetalle()
#print(__name__)  #nombre del módulo que se esta ejecutando
print('Eliminación de objetos'.center(50, '-'))
del persona1