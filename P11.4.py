def main():
    n = int(input('Entre com o valor de n inteiro >= a zero: '))
    print('     ', end = '')
    for i in range(1, n + 1):
        print('%5d' %i, end = '')
    print()
    c = ''
    for i in range(1, n + 1):
        print('%5d' %i, end = '')
        for h in range(2, i+1):
            print('     ', end = '')
        for j in range(i, n + 1):
            print("%5d" %(i*j), end = '')
        print()
while True:
    main()
