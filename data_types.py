# concatenar str (string)
grupo = "Aerosmith"
print("Mi grupo favorito es: " + grupo)
print("Mi grupo favorito es:", grupo)  # se agrega espacio en blanco al principio

n1 = 5
n2 = "4"
print(n1 + int(n2))

#Tipos boo (boolean) True/False - Se distingue entra maypus
miVar = 3 > 2
print(miVar)

if miVar:
    print("Resultado verdadero") #se respeta identación
else:
    print("Resultado falso")


#Procesar entrada #
num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))
resultado = num1 + num2
print(resultado)
print("Fin del programa")