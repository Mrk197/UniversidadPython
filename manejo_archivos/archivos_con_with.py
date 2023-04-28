#cerrado automático de archivos
#ya no se requiere try catch
from ManejoArchivos import ManejoArchivos

'''with open('prueba.txt', 'r', encoding='utf8') as archivo:
    print(archivo.read())

#se mandan a llamar:
    #__enter__ donde se abre el archivo (recurso)
    #__exit__ donde se cierra '''

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

