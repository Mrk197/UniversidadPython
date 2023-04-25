#def lista
nombres = ['Juan', 'Karla', 'Ricardo', 0]
#imprimir
print(nombres[0])
print(nombres[-1])
#pregutar largo
print(len(nombres))
#sgregar elemento
nombres.append('Lorenzo')
print(nombres)
#insertar en indice en específico
nombres.insert(1, 'Octavio')
print(nombres)
#acceder a un rango
print(nombres[0:2]) #sin incluir índice 2
print(nombres[0:4])
print(nombres[2:])
#cambiar valor
nombres[3] = 'Ivone'
print(nombres)

#iTERAR
for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista")

print("Remover")
#remover elemento
nombres.remove('Octavio')
print(nombres)
#remover último
nombres.pop()
print(nombres)
#remover un indice
del nombres[3]
print(nombres)
#limpiar lista
nombres.clear()
print(nombres)
##borrar lista por completo
del nombres
print(nombres)

