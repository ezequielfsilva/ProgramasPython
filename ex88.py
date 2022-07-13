from time import sleep
from random import randint
print('--'*20)
print('         JOGA NA MEGA SENA')
print('--'*20)
jogos = int(input('Quantos jogos você quer que eu sortei? '))
print('-='*5, f'SORTEANDO {jogos} JOGOS', '-='*5)
lista = [0, 0, 0, 0, 0, 0]
for i in range(0, jogos):
    for j in range(0, 6):
        if j == 0:
            lista[j] = randint(1, 60)
        if j >= 1:
            lista[j] = randint(1, 60)
            for l in range(0, j):
                if lista[j] == lista[l]:
                    lista[j] = randint(1, 60)
    sleep(2)
    lista.sort()
    print(f'Jogo {i+1}: {lista}')
