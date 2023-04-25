#Operadores aritméticos  + - * / // % **
opA = 3
opB = 2
suma = opA + opB
print(f'Resultado suma: {suma}') #f literal
division = opA/opB #con punto flotante
print(f'Resultado división: {division}')
division2 = opA//opB #sin punto flotante
print(f'Resultado división sin flotante: {division2}')
exponente = opA ** opB
print(f'Resultado exponente: {exponente}')

#OP de Asignación
# opA = opA +1
# opA +=1
# opA -=1
# opA *=1

#OP de Comparación  == != > <
resultado = opA == opB
resultado = opA != opB

#OP Lógicos and or not
a= True
b = False
resultado = a and b
print(f'Resultado: {resultado}')

# indicar caracter especial (caracter de escape)
print("Los 20\' y los 30 \'")