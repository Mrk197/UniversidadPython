
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') #si no existe crea archivo #w - write
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.write('Adios')
    archivo.close()
    print('Fin del archivo')
    #archivo.write('Adios')