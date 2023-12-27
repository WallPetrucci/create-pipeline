import os

class Calculadora:
    def __init__(self):
       self.envar =  os.getenv('MY_VAR')
    
    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

    def divisao(self, a, b):
        return a / b

    def multiplicacao(self, a, b):
        return a * b

    def get_env_var(self):
        return self.envar
    
    def get_a(self, a):
        return a