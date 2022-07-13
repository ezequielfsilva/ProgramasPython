def Hanoi(n, torreA, torreB, torreAux):
    if n == 1:
        # mover disco 1 da torreA para a torreB
        Movimente(1, torreA, torreB)

    else:
        # n - 1 discos da torreA para torreAux com torreB auxiliar
        Hanoi(n - 1, torreA, torreAux, torreB)
        # mover disco n da torreA para torreB
        Movimente(n, torreA, torreB)
        # n - 1 discos da torreAux para a torreB com torreA auxiliar
        Hanoi(n - 1, torreAux, torreB, torreA)
def Movimente(k, origem, destino):
    print("mover disco ", k, " da torre ", origem, " para a torre ", destino)
    if origem == 'A':
        if destino == 'B':
            push(listaB, k)
            pop(listaA)
        else:
            push(listaC, k)
            pop(listaA)
    elif origem == 'B':
        if destino == 'A':
            push(listaA, k)
            pop(listaB)
        else:
            push(listaC, k)
            pop(listaB)
    elif origem == 'C':
        if destino == 'B':
            push(listaB, k)
            pop(listaC)
        else:
            push(listaA, k)
            pop(listaC)
    listacopA = listaA[:]
    listacopB = listaB[:]
    listacopC = listaC[:]
    r = Maior(len(listaA), len(listaB), len(listaC))
    p, u, s, t, q = 0, 0, 0, 0, 0
    while True:
        if r[1] == 'A':
            print(listacopA[-1], end='     ')
            pop(listacopA)
            if len(listacopA) < len(listacopB):
                print(listacopB[-1], end='     ')
                pop(listacopB)
                t = 1
                if len(listacopA) < len(listacopC):
                    print(listacopC[-1])
                    pop(listacopC)
                    q = 1
            elif len(listacopA) == len(listacopB) and len(listacopC) <= len(listacopA):
                print()
                print(listacopA[-1], '     ', listacopB[-1], end='     ')
                pop(listacopB)
                pop(listacopA)
                t = 1
                if len(listacopA) < len(listacopC):
                    print(listacopC[-1])
                    pop(listacopC)
                    q = 1
            if len(listacopA) < len(listacopC) and len(listacopA) >= 1:
                print('     ',listacopC[-1])
                pop(listacopC)
                s = 1
                if len(listacopA) == len(listacopB):
                    print(listacopA[-1], '     ', listacopB[-1], '     ', listacopC[-1])
                    pop(listacopC)
                    pop(listacopB)
                    pop(listacopA)
                    q = 1
            elif len(listacopA) == len(listacopC):
                print()
                print(listacopA[-1], '     ', end='')
                pop(listacopA)
                s = 1
                if len(listacopA) < len(listacopB):
                    print(listacopB[-1], '     ', listacopC[-1])
                    pop(listacopB)
                    pop(listacopC)
                    q = 1
                else:
                    print('     ', listacopC[-1])
                    pop(listacopC)

        if r[1] == 'B':
            print('     ', listacopB[-1], end='     ')
            pop(listacopB)
            if len(listacopB) < len(listacopA):
                print(listacopA[-1], end='     ')
                pop(listacopA)
                t = 1
                if len(listacopB) < len(listacopC):
                    print(listacopC[-1])
                    pop(listacopC)
                    q = 1
            elif len(listacopB) == len(listacopA) and len(listacopC) <= len(listacopB):
                print()
                print(listacopA[-1], '     ', listacopB[-1], end='     ')
                pop(listacopB)
                pop(listacopA)
                t = 1
                if len(listacopB) < len(listacopC):
                    print(listacopC[-1])
                    pop(listacopC)
                    q = 1
            if len(listacopB) < len(listacopC):
                print('     ',listacopC[-1])
                pop(listacopC)
                u = 1
                if len(listacopB) == len(listacopA):
                    print(listacopA[-1], '     ', listacopB[-1], '     ', listacopC[-1])
                    pop(listacopC)
                    pop(listacopB)
                    pop(listacopA)
                    q = 1
            elif len(listacopB) == len(listacopC):
                print()
                u = 1
                if len(listacopB) < len(listacopA):
                    print(listacopA[-1], '     ', listacopB[-1], '     ', listacopC[-1])
                    pop(listacopB)
                    pop(listacopC)
                    pop(listacopA)
                    q = 1
                else:
                    print('     ', listacopB[-1],'     ', listacopC[-1])
                    pop(listacopC)
                    pop(listacopB)

        if r[1] == 'C':
            print('     ', '     ', listacopC[-1])
            pop(listacopC)
            if len(listacopC) == len(listacopA) and len(listacopC) >= len(listacopB):
                print(listacopA[-1], end='     ')
                pop(listacopA)
                s = 1
                if len(listacopB) == len(listacopC):
                    print(listacopB[-1], '     ', listacopC[-1])
                    pop(listacopC)
                    pop(listacopB)
                    q = 1
                else:
                    print('     ', listacopC[-1])
                    pop(listacopC)
            if len(listacopC) == len(listacopB):
                u = 1
                if len(listacopC) > len(listacopA):
                    print('     ', listacopB[-1],'     ', listacopC[-1])
                    pop(listacopB)
                    pop(listacopC)
                else:
                    print(listacopA[-1], '     ', listacopB[-1], '     ', listacopC[-1])
                    pop(listacopA)
                    pop(listacopB)
                    pop(listacopC)
                    q = 1
        if q == 1:
            for i in reversed(range(len(listacopA))):
                print(listacopA[i],'     ', listacopB[i],'     ', listacopC[i])
                if i == 0:
                    p = 1
        if t == 1:
            while len(listacopA) > len(listacopC):
                print(top(listacopA), '     ',top(listacopB))
                pop(listacopA)
                pop(listacopB)
                if len(listacopA) == len(listacopC):
                    for i in reversed(range(len(listacopA))):
                        print(listacopA[i], '     ', listacopB[i], '     ', listacopC[i])
                        if i == 0:
                            p = 1
        if s == 1:
            while len(listacopA) > len(listacopB):
                print(top(listacopA), '          ',top(listacopC))
                pop(listacopA)
                pop(listacopC)
                if len(listacopA) == len(listacopB):
                    for i in reversed(range(len(listacopA))):
                        print(listacopA[i], '     ', listacopB[i], '     ', listacopC[i])
                        if i == 0:
                            p = 1
        if u == 1:
            while len(listacopB) > len(listacopA):
                print('     ', top(listacopB), top(listacopC))
                pop(listacopB)
                pop(listacopC)
                if len(listacopB) == len(listacopA):
                    for i in reversed(range(len(listacopA))):
                        print(listacopA[i], '     ', listacopB[i], '     ', listacopC[i])
                        if i == 0:
                            p = 1
        if p == 1:
            break
    print('A', '     B', '     C')

# Empilha novo elemento
def push(P, x):
    P.append(x)
# Retorna o elemento do topo da pilha mas não desempilha
def top(P):
    if is_empty(P): return None
    return P[-1]
# Remove elemento do topo da pilha
def pop(P):
    return P.pop()

def Maior(a, b, c):
    maior = a
    coluna = 'A'
    if b > a and b > c:
        maior = b
        coluna = 'B'
    if c > a and c > b:
        maior = c
        coluna = 'C'
    return maior, coluna

listaA = []
listaB = []
listaC = []
# Exemplos de chamadas
print("\n* * * Movimentar 3 discos * * *")
for k in reversed(range(1, 3)):
    push(listaA, k)
for k in range(1, 3):
    print(k)
    if k == 2:
        print('A', '     B', '     C')
lista1 = listaA[:]
Hanoi(, 'A', 'B', 'C')
#print("\n* * * Movimentar 3 discos * * *")
#for k in range(1, 4):
#    print(k)
#    if k == 3:
#        print('A', '     B', '     C')
#Hanoi(3, 'A', 'B', 'C')