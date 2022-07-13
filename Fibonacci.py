n = int(input('Entre com o valor de N: '))
print(f'Sequência de Fibonacci - menores ou iguais a {n}')
i = 1
j = 1
print(i)
print(j)
while True:
    k = i + j
    if k > n:
        break
    print(k)
    i = j
    j = k


