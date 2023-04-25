class Aritmetica:
    #DocString
    """
    Clase Aritemetica para realizar las opraciones de sumas, restar, etc.
    """
    def __init__(self, opA, opB):
        self.operandoA = opA
        self.operandoB = opB

    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetia1 = Aritmetica(7, 8)
print(aritmetia1.sumar())
print(aritmetia1.restar())
print(aritmetia1.multiplicar())
print(f'{aritmetia1.dividir():.2}') #redondea