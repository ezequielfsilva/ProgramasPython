# Nome: EZEQUIEL FERREIRA DA SILVA
# NUSP: 10092486
# Exercício 1

# função mdc
def mdc(n, m):
    resto = n % m
    while resto != 0:
        n = m
        m = resto
        resto = n % m
    return m

class Fração:
    '''Define a classe Fração Ordinária.'''
    #Construtor da classe
    def __init__(self, numerador = 0, denominador = 1):
        '''Cria uma instância de Fração.'''
        if type(numerador) != int:
            raise ValueError("As entradas das Frações precisam ser números inteiros")
        if type(denominador) != int:
            raise ValueError("As entradas das Frações precisam ser números inteiros")
        if denominador == 0:
            raise ValueError("Denominador igual a zero")
        if denominador < 0:
            self.num = - numerador
            self.den = - denominador
        else:
            self.num = numerador
            self.den = denominador

     #Retorna a soma de dois elementos da classe
    def __add__(self, p1):
         xnum = self.num * p1.den + self.den * p1.num
         xden = self.den * p1.den
         xmdc = mdc(xnum, xden)
         return Fração(xnum // xmdc, xden // xmdc)

     #Retorna a subtração de dois elementos da classe
    def __sub__(self, p1):
         xnum = self.num * p1.den - self.den * p1.num
         xden = self.den * p1.den
         xmdc = mdc(xnum, xden)
         return Fração(xnum // xmdc, xden // xmdc)

     #Retorna a multiplicação de dois elementos da classe
    def __mul__(self, p1):
         xnum = self.num * p1.num
         xden = self.den * p1.den
         xmdc = mdc(xnum, xden)
         return Fração(xnum // xmdc, xden // xmdc)

     #Retorna a divisão de dois elementos da classe
    def __truediv__(self, p1):
        xnum = self.num * p1.den
        xden = self.den * p1.num
        xmdc = mdc(xnum, xden)
        return Fração(xnum // xmdc, xden // xmdc)

     #Retorna a potência de um elemento da classe
    def __pow__(self, power, modulo=None):
        if type(power) != int:
            raise ValueError("O EXPOENTE precisa ser um número inteiro")
        if power <= -1:
            xnum = self.den ** (-power)
            xden = self.num ** (-power)
            xmdc = mdc(xnum, xden)
        else:
            xnum = self.num ** power
            xden = self.den ** power
            xmdc = mdc(xnum, xden)
        return Fração(xnum // xmdc, xden // xmdc)

     #Compara dois elementos da classe (igual)
    def __eq__(self, p1):
        pri_fator = self.num * p1.den
        seg_fator = self.den * p1.num
        return pri_fator == seg_fator

     #Compara dois elementos da classe (diferente)
    def __ne__(self, p1):
        pri_fator = self.num * p1.den
        seg_fator = self.den * p1.num
        return pri_fator != seg_fator

     #Compara dois elementos da classe (maior)
    def __gt__(self, p1):
        pri_fator = self.num * p1.den
        seg_fator = self.den * p1.num
        return pri_fator > seg_fator

     #Compara dois elementos da classe (maior ou igual)
    def __ge__(self, p1):
        pri_fator = self.num * p1.den
        seg_fator = self.den * p1.num
        return pri_fator >= seg_fator

     #Compara dois elementos da classe (menor)
    def __lt__(self, p1):
        pri_fator = self.num * p1.den
        seg_fator = self.den * p1.num
        return pri_fator < seg_fator

     #Compara dois elementos da classe (menor ou igual)
    def __le__(self, p1):
        pri_fator = self.num * p1.den
        seg_fator = self.den * p1.num
        return pri_fator <= seg_fator

     #Transforma em string para o print
    def __str__(self):
        if self.den != 1:
            return str(self.num) + "/" + str(self.den)
        else:
            return str(self.num)

# testes da classe
if __name__ == "__main__":
    x = Fração(2, 6)
    y = Fração(2, 12)
    z = Fração()
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x ** -1)
    print(x ** 2)
    print(x == y)
    print(x != y)
    print(x > y)
    print(x >= y)
    print(x < y)
    print(x <= y)
    print(z)