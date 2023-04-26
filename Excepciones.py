#se utliizan para regresar errores y evitar que programa termine de manera abrupta

from excepcion_personalizada import NumerosIdenticosException

#división entre cero
#con clase padre
try:
    10/0
except Exception as e: #se usa la clase padre de ZeroDivisionError y se renombra como e
    print(f'Ocurrio un error: {e}')

#más específico
try:
    10/0
except ZeroDivisionError as e: #solo puede manejar excepciones de este tipo su da otro tipo se da error (termina programa)
    print(f'Ocurrio un error: {e}')


#Procesamiento de excepciones
resultado = None
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))

#PERSONALIZADA
    if a == b:
        raise NumerosIdenticosException('Numeros identicos') #raise permite arrojar una excepción
    resultado = a / b

except ZeroDivisionError as e:
    print(f'Ocurrio un error de ZDE: {e}, {type(e)}')
except TypeError as e:
    print(f'Ocurrio un error de Type: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio otro tipo de error: {e}, {type(e)}')
# ELSE Y FINALLY
else: #si no se ejecuta alguna excepció
    print('No se arrojó ninguna excepción')
finally: #se ejecuta siempre
    print('Ejecución de bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')






