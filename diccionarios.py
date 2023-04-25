#coleccion de datos organizado por clave y valor
#no hay indice, se accede con la llave (key)
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Managment System'
}
print(diccionario)
#largo
print(len((diccionario)))
#acceder a un elemento
print(diccionario['IDE'])
#op 2
print(diccionario.get('OOP'))
#modificnado
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)
#recorrer elementos
for termino in diccionario:
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

#comprobar si ya existe un elemento
print('IDe' in diccionario)
#agregar elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
#remover un elemento
diccionario.pop('DBMS')
print(diccionario)
#limpiar
diccionario.clear()
print(diccionario)
#eliminar por completo
del diccionario
print(diccionario)