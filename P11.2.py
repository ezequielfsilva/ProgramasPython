def main():
    while True:
        try:
            n = int(input('Entre com o valor de n inteiro >= a zero: '))
            if n < 0:
                print('>>>>> ERRO!! Digite um número inteiro n >= a zero.')
                continue
        except:
            print('>>>>> ERRO!! Digite um número inteiro n >= a zero.')
        else:
            while True:
                try:
                    m = int(input('Entre com o valor de m inteiro >= a zero: '))
                    if m < 0:
                        print('>>>>> ERRO!! Digite um número inteiro m >= a zero.')
                        continue
                except:
                    print('>>>>> ERRO!! Digite um número inteiro m >= a zero.')
                else:
                    a = 0
                    while a <= m:
                        if a == 1:
                            print('     ', end = '')
                        if a >= 1:
                            print('%5d' %a, end = '')
                        a += 1
                    print()
                    a = 1
                    while a <= n:
                        print('%5d' %a, end = '')
                        b = 1
                        while b <= m:
                            c = a*b
                            print('%5d' %c, end = '')
                            b += 1
                        a += 1
                        print()
                if m >= 0:
                    break

main()
