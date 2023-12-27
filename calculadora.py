import os

class Calculadora:
    def __init__(self):
        print(f"VARIAVEL DE AMBIENTE - {os.getenv('MY_VAR')}")
    
    def soma(self, a, b):
        return a + b

calculadora = Calculadora()
print(calculadora.soma(5, 5))