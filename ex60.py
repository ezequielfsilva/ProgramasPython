from math import factorial
##Pode-se fazer o programa utilizando o modulo 'factorial'

n = int(input("Digite um valor para calcular o seu fatorial: "))
f = 1
while n > 0:
    print("{}".format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print(f)