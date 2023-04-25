#No se pueden modificar, agregar, eliminar  (ES INMUTABLE)

#Definir
frutas = ('Naranja', 'Platano', 'Guayaba') #si es 1 elemento => ('Naranja',) -para dif. de string
print(frutas)
#saber largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#acceder a la inversa
print(frutas[-1])
#en un rango
print(frutas[0:1]) #('Naranja',)
#recorrer
for fruta in frutas:
    print(fruta, end=' ')
#cambiar valor tupla
#frutas[0] = 'Pera' X
frutaLista = list(frutas)
frutaLista[0] = 'Pera'
frutas = tuple(frutaLista)
print('\n', frutas)
#aliminar tupla
del frutas
print(frutas)