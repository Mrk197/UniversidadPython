#No es posible modificar pero si agregar/eliminar
#No tiene indices, el orden es aleatorio

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento esta presente
print('Martes' in planetas)
#agragar elementos
planetas.add('Tierra')
print(planetas)
#no acepta elementos duplicados
planetas.add('Tierra')
print(planetas) #sólo aparece un elemento Tierra
#eliminar elemento
#planetas.remove('Tierras') #arroja error si no se encuentra
print(planetas)
planetas.discard('Jupiters') #no arroja error
print(planetas)
#limpiar
planetas.clear()
print(planetas)
#eliminar por completo
del planetas
print(planetas)