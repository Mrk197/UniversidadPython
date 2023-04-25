def sumar(a, b) ->int:  #es sólo un indiciio del tipo de dato que se va a retornar, no olbiga a regresar este tipo
    return a+b
print(sumar(5,8))


def listarNombres(*nombres): #se desconoce la cantidad de elementos, lo convierte a tupla
    for nombre in nombres:
        print(nombre)
listarNombres('Juan', 'Karla', 'Maria')


def listarTerminos(**kwargs): #para recibir como argumento un diccionario
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')


#MANEJO DE DIFERENTES TIPOS DE DATOS
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Roberto']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((10, 11))


#FUNCION RECURSIVA
def factorial (n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(f'factorial de 5: {factorial(5)}')