def somainvfat():
    def fat(k):
        f = 1
        for j in range(2, k +1):
            f = f*j
        return f
    while True:
        try:
            n = int(input('Entre com um valor de n inteito maior que zero: '))
        except:
            print('ERRO!! Entrada inválida. Digite um número inteiro.')
        else:
            if n <= 0:
                print('ERRO!! Entrada inválida. Digite um número inteiro > que zero.')
                continue
            else:
                soma = 0
                for i in range(1, n + 1):
                    invfat = 1/fat(i)
                    soma = soma + invfat
                    if i < n:
                        print('1/{}!'.format(i), end = ' + ')
                    else:
                        print('1/{}!'.format(i))
                print('\nSoma acima é igual a ', soma)
                print()
                break
while True:
    somainvfat()