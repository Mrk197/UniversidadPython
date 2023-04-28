
#archivo = open('C:\\Users\\SOPORTE\\PycharmProjects\\UniversidadPython\\manejo_archivos\\prueba.txt', 'r', encoding='utf8')
archivo = open('prueba.txt', 'r', encoding='utf8')
#print(archivo.read())

"""# leer algunos caracteres
print(archivo.read(5)) #primeros 5
print(archivo.read(3)) #siguientes 3
#leer lineas completas
print(archivo.readline())
print(archivo.readline())

#iterrar el archivo
for linea in archivo:
    print(linea)
    
#leer lineas
print(archivo.readlines()[0]) #retorna una lista, se esta imprimiendo la primera linea   
"""

#abrimos un nuevo archivo
# a - anezar info
archivo2 = open('copia.txt', 'a', encoding='utf8')  # a-agrega información y w-sobreescribe
archivo2.write(archivo.read())
archivo.close() #se recomienda siempre cerrar los archivos
archivo2.close()

print("se ha terminado el proceso de copia")


