"""Função Seno e Cosseno calculadas pela Série de Taylor e pela biblioteca math"""
def sencoss(entradaX, n):
    def fat(k):
        f = 1
        for j in range(2, k + 1):
            f = f * j
        return f

    soma, soma2 = 0, 0
    pot, pot2 = entradaX, 1
    for i in range(0, n):
        soma = soma + pot / fat(2 * i + 1)
        soma2 = soma2 + pot2 / fat(2 * i)
        pot = -pot * entradaX * entradaX
        pot2 = -pot2 * entradaX * entradaX
    return soma, soma2
    #return soma2

cont = 0
while True:
    if cont != 0:
        continuar = input('Deseja continuar? [S/N] ').upper()
        if len(continuar) == 1 and continuar == 'N':
            break
        elif len(continuar) != 1:
            print("ERRO!! Entrada inválida. Digite 'S' ou 'N'")
            continue
        elif len(continuar) == 1 and continuar != 'S' and continuar != 'N':
            print("ERRO!! Entrada inválida. Digite 'S' ou 'N'")
            continue
        elif len(continuar) == 1 and continuar == 'S':
            print()
    import math
    c = 0
    while True:
        if c == 1:
            entradaX = antigovalorX
        else:
            entradaX = input('Entre com o x: ')
        c = 0
        try:
            entradaX = float(entradaX)
            if entradaX < 0 or entradaX > 2 * math.pi:
                print('>>>>> ERRO!! Entre com o x entre 0 e {}'.format(2 * math.pi))
                continue
        except:
            if cont != 0:
                if len(entradaX) == 0:
                    c = 1
                    continue
            print('>>>>> ERRO!! Entrada inválida.')
            continue
        else:
            while True:
                if c == 1:
                    n = antigovalorN
                else:
                    n = input('Entre com o valor de n inteiro no intervalo de 1 a 100: ')
                c = 0
                try:
                    n = int(n)
                    if n <= 0 or n >= 101:
                        print('>>>>> ERRO!! Inteiro digitado fora do intervalo permitido.')
                        continue
                except:
                    if cont != 0:
                        if len(n) == 0:
                            c = 1
                            continue
                    print('>>>>> ERRO!! Entrada inválida.')
                else:
                    break
        break
    from time import process_time
    t = process_time()
    serietaylor = sencoss(entradaX, n)
    t = process_time() - t
    t2 = process_time()
    a = math.sin(entradaX)
    t2 = process_time() - t2
    t3 = process_time()
    b = math.cos(entradaX)
    t3 = process_time() - t3
    antigovalorX = entradaX
    antigovalorN = n
    cont += 1
    print('\nValores calculados para:')
    print('x =', entradaX, '\nn =', n)
    print('\nSeno:')
    print('Usando a soma de termos: {}  -  tempo: {}'.format(serietaylor[0], t))
    print('Usando a função Seno:    {}  -  tempo: {}'.format(a, t2))
    print('\nCosseno:')
    print('Usando a soma de termos: {}  -  tempo: {}'.format(serietaylor[1], t))
    print('Usando a função Cosseno: {}  -  tempo: {}'.format(b, t3))
    print('\n* * * * * * * * *')
    print()
