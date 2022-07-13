def main():
    n = int(input('Gigite um número n inteiro > que zero: '))
    import math
    soma = 0
    for k in range(2, n + 1):
        for i in range(2, int(math.sqrt(k)) + 1):
            if k % i == 0:
                break
        else:
            soma += k
    print('A soma dos números primos menores ou iguais a {} é {} '.format(n, soma))
while True:
    main()