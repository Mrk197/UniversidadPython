class MiClase:
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variables_instancia = variable_instancia

    #método estático
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    #método de clase
    @classmethod
    def metodo_clase(cls):  #cls - class -> hace referencia a la clase
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variables_instancia)

#La variable de clase se asocia con la clase en si y no con el objeto
print(MiClase.variable_clase)

miObj = MiClase('Valor variable instancia')
print(miObj.variables_instancia) #variable diferente para cada obj
print(miObj.variable_clase) #se ve el mismo valor en todos los objetos

#Se puede asocia una nueva variable a la clase ya que Python es dinámico
MiClase.variable_clase2 = 'Valor de clase 2'

miObj2 = MiClase('Otro valor variable de instancia')
print(miObj2.variables_instancia)
print(miObj2.variable_clase)
print(miObj2.variable_clase2)

print("Estático")
MiClase.metodo_estatico()
print("Clase")
MiClase.metodo_clase()

miObjeto1 = MiClase('variable_instancia')
miObjeto1.metodo_clase()
print("Instancia")
miObjeto1.metodo_instancia()
