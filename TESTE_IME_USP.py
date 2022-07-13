class PilhaLista:
    def __init__(self):
        self._pilha = [] # lista que conterá a pilha
     # retorna o tamanho da pilha
    def __len__ (self):
        return len(self._pilha)
     # retorna True se pilha vazia
    def is_empty(self):
        return len(self._pilha) == 0
     # empilha novo elemento e
    def push(self, e):
        self._pilha.append(e)
     # retorna o elemento do topo da pilha sem retirá-lo
     # exceção se pilha vazia
    def top(self):
        if self.is_empty( ):
            raise Empty("Pilha vazia")
        return self._pilha[-1]
     # desempilha elemento

     # excessão se pilha vazia
    def pop(self):
        if self.is_empty( ):
            raise Empty("Pilha vazia")
        return self._pilha.pop( )
# testes
P = PilhaLista()
print(P)
P.push(1)
P.push("tipo de elemento")
P.push((5, 4, 3))
P.push(True)
lista = []
for i in range(len(P)):
    lista.insert(0, P.top())
    P.pop()
print(lista)
print(lista[-1])
print(lista[-2])
print("tamanho da pilha = ", len(P))



for k in listaA:
    if destino == k:
        push(listaB, k)
        pop(listaA)
    if destino == 'C':
        push(listaC, k)
        pop(listaA)
if k in listaB:
    if destino == 'A':
        push(listaA, k)
        pop(listaB)
    if destino == 'C':
        push(listaC, k)
        pop(listaB)
if k in listaC:
    if destino == 'A':
        push(listaA, k)
        pop(listaC)
    if destino == 'B':
        push(listaB, k)
        pop(listaC)
auxlisA = listaA[:]
auxlisB = listaB[:]
auxlisC = listaC[:]

for i in reversed(range(1, len(listaA) + len(listaB) + len(listaC) + 1)):
    if len(auxlisA) > len(auxlisB) and len(auxlisB) >= len(auxlisC):
        print(auxlisA[i])
        pop(auxlisA)
    elif len(auxlisA) > len(auxlisB) and len(auxlisA) > len(auxlisC):
        print(auxlisA[i])
        pop(auxlisA)
    elif len(auxlisA) > len(auxlisB) and len(auxlisA) == len(auxlisC):
        print(auxlisA[i], '          ', auxlisC[i])
        pop(auxlisA)
        pop(auxlisC)
    elif len(auxlisA) == len(auxlisB) and len(auxlisB) > len(auxlisC):
        print(auxlisA[i], '     ', auxlisB[i])
        pop(auxlisA)
        pop(auxlisB)
    elif len(auxlisA) == len(auxlisB) == len(auxlisC):
        print(auxlisA[i], '     ', auxlisB[i], '          ', auxlisC[i])
        pop(auxlisA)
        pop(auxlisB)
        pop(auxlisC)
    elif len(listaC) >= len(listaA) and len(listaC) >= len(listaB):
        print('         ', listaC[-1])
        pop(listaC)
    if i == len(listaA) + len(listaB) + len(listaC):
        print('A', '     B', '     C')