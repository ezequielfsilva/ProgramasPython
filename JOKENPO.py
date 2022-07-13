from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogada = int(input("Qual a sua jogada? "))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('***'*11)
print('O jogador jogou {}'.format(itens[jogada]))
print('O computador jogou {}'.format(itens[computador]))
print('***'*11)
if computador == 0:
    if jogada == 0:
        print("EMPATE")
    elif jogada == 1:
        print("Jogador venceu!")
    elif jogada == 2:
        print('Computador ganhou!')
    else:
        print("jogada inválida! ")

elif computador == 1:
    if jogada == 0:
        print("Computador ganhou!")
    elif jogada == 1:
        print("EMPATE!")
    elif jogada == 2:
        print('Jogador venceu!')
    else:
        print("jogada inválida! ")

elif computador == 2:
    if jogada == 0:
        print("Jogador venceu!")
    elif jogada == 1:
        print("Computador ganhou!")
    elif jogada == 2:
        print('EMPATE!')
    else:
        print("jogada inválida! ")


