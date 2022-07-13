from random import randint
from time import sleep
computador = randint(0, 5)
print("--==-"*20)
print("\033[7;34mVou pensar em um número inteiro entre 0 e 5. Tente adivinhar...\033[m")
print("-==--"*20)
jogador = int(input("\033[1;33mEm que número eu pensei? \033[m"))
print("Processando...")
sleep(3)
if jogador == computador:
    print("\033[1;32mParabéns, você me venceu!! Eu pensei no numero {} e você escolheu {}, que é o mesmo número.\033[m".format(computador, jogador))
else:
    print("\033[1;31mEu venci! Eu pensei no número {} e não no número {}.\033[m".format(computador, jogador))
