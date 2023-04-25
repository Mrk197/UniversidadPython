#división entre cero
#con clase padre
try:
    10/0
except Exception as e: #se usa la clase padre de ZeroDivisionError y se renombra como e
    print(f'Ocurrio un error: {e}')
#más específico
try:
    10/0
except ZeroDivisionError as e: #solo puede manejar excepciones de este tipo su da otro tipo se da error
    print(f'Ocurrio un error: {e}')

#Procesamiento de excepciones
resultado = None
a = '10'
b = 0
try:
    resultado = a / b
except Exception as e:
    print(f'Ocurrio un error: {e}')

print(f'Resultado: {resultado}')
print('Continuamos...')