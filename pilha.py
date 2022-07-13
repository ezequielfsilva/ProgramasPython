# Exercício Programa I – MAC 122 – PDA
# Ezequiel Ferreira da Silva
# NUSP: 10092486

class PilhaLista:
    '''Pilha como uma lista.'''
    # Construtor da classe PilhaLista
    def __init__(P):
        P._pilha = [] # lista que conterá a pilha

     # retorna o tamanho da pilha
    def __len__(P):
        return len(P._pilha)

     # retorna True se pilha vazia
    def is_empty(P):
        return len(P._pilha) == 0

     # empilha novo elemento
    def push(P, x):
        P._pilha.append(x)

     # retorna o elemento do topo da pilha sem retirá-lo
     # exceção se pilha vazia
    def top(P):
        if P.is_empty():
            return None
        return P._pilha[-1]

     # desempilha elemento
     # excessão se pilha vazia
    def pop(P):
        if P.is_empty():
            raise ValueError("Pilha vazia")
        return P._pilha.pop( )

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

    def __str__(self):
        if self.den != 1:
            return str(self.num) + "/" + str(self.den)
        else:
            return str(self.num)

def TraduzPosFixa(expnova):
    cont = 0
    mp = PilhaLista()
    oper = PilhaLista()
    #Percorrer a expressão, verificar as preferencias e montar a expressão pós-fixa
    for i in range(len(expnova)):
        if '0' <= expnova[i] <= '9':
            mp.push(expnova[i])
        if expnova[i] == '**':
            oper.push(expnova[i])
        if expnova[i] == '*' or expnova[i] == '/':
            if oper.top() == '**':
                mp.push(oper.top)
                oper.pop()
            if oper.top() == '*' or oper.top() == '/':
                mp.push(oper.top())
                oper.pop()
                oper.push(expnova[i])
            else:
                oper.push(expnova[i])
        if expnova[i] == '+' or expnova[i] == '-':
            if oper.top() == '**':
                mp.push(oper.top())
                oper.pop()
            if oper.top() == None:
                oper.push(expnova[i])
            else:
                if cont == 0:
                    for j in range(len(oper)):
                        mp.push(oper.top())
                        oper.pop()
                elif oper.top() == '(':
                    pass
                else:
                    for j in range(len(oper)):
                        mp.push(oper.top())
                        oper.pop()
                        if oper.top() == "(":
                            break
                oper.push(expnova[i])
        if expnova[i] == "(":
            oper.push(expnova[i])
            cont += 1
        if expnova[i] == ")":
            for j in range(len(oper)):
                mp.push(oper.top())
                oper.pop()
                if oper.top() == "(":
                    oper.pop()
                    break
            cont -= 1

    for i in range(len(oper)):
        mp.push(oper.top())
        oper.pop()
    return mp

def CalcPosFixa(listaexp):
    lista = []
    lista2 = PilhaLista()
    #Varrer a expressão pós-fixa e realizar os calculos
    for i in range(len(listaexp)):
        lista.insert(0, listaexp.top())
        listaexp.pop()
    while len(lista) != 0:
        if '0' <= lista[0] <= '9':
            lista2.push(int(lista[0]))
            del(lista[0])
        elif lista[0] == '+':
            x = lista2.top()
            lista2.pop()
            z = lista2.top() + x
            lista2.pop()
            lista2.push(z)
            del(lista[0])

        elif lista[0] == '-':
            x = lista2.top()
            lista2.pop()
            z = lista2.top() - x
            lista2.pop()
            lista2.push(z)
            del (lista[0])
        elif lista[0] == '*':
            x = lista2.top()
            lista2.pop()
            z = lista2.top() * x
            lista2.pop()
            lista2.push(z)
            del (lista[0])
        elif lista[0] == '/':
            x = lista2.top()
            lista2.pop()
            z = lista2.top() / x
            lista2.pop()
            lista2.push(z)
            del (lista[0])
        elif lista[0] == '**':
            x = lista2.top()
            lista2.pop()
            z = lista2.top() ** x
            lista2.pop()
            lista2.push(z)
            del (lista[0])
    return lista2.top()

while True:
    #Entrada do usuário
    exp = input(">>> ")
    import re
    t = exp
    expnova = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", t)
    for i in range(len(expnova)):
        if expnova[i] == '*' and expnova[i+1] == '*':
            expnova.pop(i+1)
            expnova[i] = '**'
            break
    #Chamar função de tradução da expressão
    a = TraduzPosFixa(expnova)
    #Chamar função de cálculo da expressão
    b = CalcPosFixa(a)
    #Mostrar ao usuário o valor da expressão digitada
    print(b)
    contin = input('Digite "FIM" para encerrar o programa: ').upper()
    if contin == 'FIM':
        break