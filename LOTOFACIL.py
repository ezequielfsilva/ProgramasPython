import random
from time import sleep
a = [13, 10, 20, 11, 24, 14, 25, 3, 4]
b = [19, 1, 18, 2, 5, 17, 22, 23, 9]
c = [12, 15, 21, 6, 7, 16, 8]
print('Iniciando o programa...')
#sleep(1)
print('\nOlá! Bem vindo(a) aos números da SORTE da Lotofácil.\nEsse programa seleciona 15 números de um total de 25 levando em consideração alguns parâmetros e metodologia específica.')
#sleep(4)
print(' \n PARÂMETROS: \n   Os MELHORES 9 números em relação à frequência de aparição nos sorteios       A = {} \n   Os INTERMEDIÁRIOS 9 números em relação à frequência de aparição nos sorteios B = {} \n   Os PIORES 7 números em relação à frequência de aparição nos sorteios         C = {}'.format(a, b, c))
print('\nPrimeiro você terá que selecionar quantos números PARES e IMPARES deseja no seu jogo. (OBS: Você escolhendo um, automaticamente escolhe o outro)')
#sleep(4)
pares = int(input('Quantos números PARES você deseja no seu jogo? '))
impares = 15 - pares
sleep(0.5)
print('\nLogo, seu JOGO conterá {} PARES e {} IMPARES.'.format(pares, impares))
#sleep(2)
print('\nAgora você terá que selecionar quantos números deseja das listas A, B e C. Lembrando que a soma das três quantidades selecionadas tem que ser igual a 15.')
#sleep(3)
print('\n')
a1 = int(input('Quantos números você deseja da lista A = {} '.format(a)))
b1 = int(input('Quantos números você deseja da lista B = {} '.format(b)))
c1 = 15 - a1 - b1
sleep(0.5)
print('\nPortanto, da lista A serão {} números, da lista B serão {} números e da lista C serão {} números.'.format(a1, b1, c1))
print('\n')
print('Sorteando seus números da sorte...')
#sleep(3)
lista = []
lista1 = []
lista2 = []
jogo = []
lista3 = []
j = 0
par = 0
while j == 0 or par != pares:
    i = 0
    while i <= a1 -1:
        escolhido = random.choice(a)
        if i >= 1:
            while escolhido in lista:
                escolhido = random.choice(a)
                if escolhido not in lista:
                    break
        lista.append(escolhido)
        jogo.append(escolhido)
        i += 1
    i = 0
    while i <= b1 -1:
        escolhido1 = random.choice(b)
        if i >= 1:
            while escolhido1 in lista1:
                escolhido1 = random.choice(b)
                if escolhido1 not in lista1:
                    break
        lista1.append(escolhido1)
        jogo.append(escolhido1)
        i += 1
    i = 0
    while i <= c1 -1:
        escolhido2 = random.choice(c)
        if i >= 1:
            while escolhido2 in lista2:
                escolhido2 = random.choice(c)
                if escolhido2 not in lista2:
                    break
        lista2.append(escolhido2)
        jogo.append(escolhido2)
        i += 1

    lista_ordenada = sorted(lista)
    lista1_ordenada = sorted(lista1)
    lista2_ordenada = sorted(lista2)
    jogo1 = sorted(jogo)
    lista.clear()
    lista1.clear()
    lista2.clear()
    jogo.clear()
    for i in range(0, 15):
        if jogo1[i] % 2 == 0:
            par += 1
    for i in range(0, 11):
        if jogo1[i]+1 == jogo1[i+1] == jogo1[i+2] -1 == jogo1[i+3] -2 == jogo1[i+4] -3:
            j += 1
    if j == 0 and par == pares:
            par = 0
    for i in range(0, 10):
        if jogo1[i]+1 == jogo1[i+1] == jogo1[i+2] -1 == jogo1[i+3] -2 == jogo1[i+4] -3 == jogo1[i+5] -4:
            j = 0
            par = 0



print(65*'==')
print(f'                         {jogo1}')
print(65*'==')
