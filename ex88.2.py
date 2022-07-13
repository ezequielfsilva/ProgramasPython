from time import sleep
from random import randint
lista =[]

print('--'*20)
print('         JOGA NA MEGA SENA')
print('--'*20)
n = int(input('Quantos jogos você quer que eu sortei? '))
print('-='*5, f'SORTEANDO {n} JOGOS', '-='*5)
tot = 1
while tot <= n:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    tot += 1
    lista.sort()
    sleep(1)
    print(f'Jogo {tot-1}: {lista}')
    lista.clear()
print('BOA SORTE! *--*')