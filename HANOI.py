#Exercicios 2
#Ezequiel Ferreira da Silva
#NUSP 10092486

#Função recursiva
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

#Função que movimenta os discos nas colunas A, B e C
def Movimente(k, origem, destino):
    print("mover disco ", k, " da torre ", origem, " para a torre ", destino)
    if origem == 'A':
        if destino == 'B':
            #Empilha na pilha B o elemento K
            push(listaB, k)
            pop(listaA)
        else:
            # Empilha na pilha C o elemento K
            push(listaC, k)
            pop(listaA)
    elif origem == 'B':
        if destino == 'A':
            # Empilha na pilha A o elemento K
            push(listaA, k)
            pop(listaB)
        else:
            # Empilha na pilha C o elemento K
            push(listaC, k)
            pop(listaB)
    elif origem == 'C':
        if destino == 'B':
            # Empilha na pilha B o elemento K
            push(listaB, k)
            pop(listaC)
        else:
            # Empilha na pilha A o elemento K
            push(listaA, k)
            pop(listaC)
    q, r, p = 0, 0, 0
    #Calcula qual valor é maior dos três
    x = Maior(len(listaA), len(listaB), len(listaC))
    #varrer as pilhas A, B e C e imprimir
    for i in reversed(range(x[0])):
        b = 0
        a = 0
        #TRY para tratar o erro das pilhas terem tamanhos distintos
        try:
            int(listaA[i])
        except:
            pass
        else:
            a = 1
            # (a = 1, b = 1) para ajudar no espaçamento do print entre um número de uma pilha e outra
            if p == 1:
                print()
                print(listaA[i], end='')
            else:
                print()
                print(listaA[i], end='')
                p = 1
                # (p = 1, q = 1) para diferenciar quando veio da mesma pilha, para não imprimir junto\colado

        try:
            int(listaB[i])
        except:
            pass
        else:
            b = 1
            if q == 1:
                if a == 0:
                    print()
                    print('       ',listaB[i], end='')
                else:
                    print('      ', listaB[i], end='')
                q = 1
            else:
                if a == 0:
                    print('       ',listaB[i], end='')
                else:
                    print('      ', listaB[i], end='')
                q = 1

        try:
            int(listaC[i])
        except:
            pass
        else:
            if b == 0 and a == 0:
                print('        ','      ',listaC[i])
            if b == 0 and a == 1:
                print('      ','       ',listaC[i])
            if b == 1 and a == 1:
                print('      ', listaC[i])
            if b == 1 and a == 0:
                print('      ', listaC[i])


    print()
    print('A','      B','      C')
listaA = []
listaB = []
listaC = []

# Empilha um elemento ao topo da pilha
def push(P, x):
    P.append(x)
# Retorna o elemento do topo da pilha mas não desempilha
def top(P):
    if is_empty(P): return None
    return P[-1]
# Remove elemento do topo da pilha
def pop(P):
    return P.pop()

#Calcula o maior entre 3 números
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

# Exemplos de chamadas
print("\n* * * Movimentar 3 discos * * *")

for k in reversed(range(1, 8)):
    push(listaA, k)
for k in range(1, 8):
    print(k)
    if k == 7:
        print('A', '     B', '     C')
Hanoi(7, 'A', 'B', 'C')


