print('=-=='*20)
print('         VAMOS JOGAR PAR OU ÍMPAR')
print('=-=='*20)
p = 0
count = 0
from random import randint
while True:
    num = int(input("Digite um valor: "))
    j = str(input("Par ou ímpar? [P/I]")).upper().strip()
    computador = randint(1, 10)
    if num % 2 == 0 and computador % 2 == 0:
        if j == 'P':
            x = num + computador
            print("---" * 20)
            print("Você jogou {} e o computador {}. Total de {} DEU {}".format(num, computador, x, 'PAR' if x % 2 == 0 else 'ÍMPAR'))
            print("---" * 20)
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print('=-==' * 20)
        else:
            x = num + computador
            print("---" * 20)
            print("Você jogou {} e o computador {}. Total de {} DEU {}".format(num, computador, x,'PAR' if x % 2 == 0 else 'ÍMPAR'))
            print("---" * 20)
            print("Você PERDEU!")
            p += 1
    elif num % 2== 1 and computador % 2 == 1:
        if j == 'P':
            x = num + computador
            print("---" * 20)
            print("Você jogou {} e o computador {}. Total de {} DEU {}".format(num, computador, x, 'PAR' if x % 2 == 0 else 'ÍMPAR'))
            print("---" * 20)
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print('=-==' * 20)
        else:
            x = num + computador
            print("---" * 20)
            print("Você jogou {} e o computador {}. Total de {} DEU {}".format(num, computador, x, 'PAR' if x % 2 == 0 else 'ÍMPAR'))
            print("---" * 20)
            print("Você PERDEU!")
            p += 1
    else:
        if j == 'I':
            x = num + computador
            print("---" * 20)
            print("Você jogou {} e o computador {}. Total de {} DEU {}".format(num, computador, x, 'PAR' if x % 2 == 0 else 'ÍMPAR'))
            print("---" * 20)
            print("Você VENCEU!")
            print("Vamos jogar novamente...")
            print('=-==' * 20)
        else:
            x = num + computador
            print("---" * 20)
            print("Você jogou {} e o computador {}. Total de {} DEU {}".format(num, computador, x, 'PAR' if x % 2 == 0 else 'ÍMPAR'))
            print("---" * 20)
            print("Você PERDEU!")
            p += 1
    if p == 1:
        break
    count += 1
print ("GAME OVER! Você venceu {} vezes.".format(count))
