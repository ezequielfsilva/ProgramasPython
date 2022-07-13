def VerificaCPF():
    m = str(input('Entre com um CPF: '))
    try:
        a = int(m)
    except:
        print('*** CPF inválido 1')
    else:
        print(a)
        if len(m) != 11:
            print('*** CPF inválido 2')
        else:
            c = []
            while True:
                if len(c) == 11:
                    break
                digito = a % 10
                c.append(digito)
                a = a // 10
            soma = 0
            for i in range(0, 9):
                z = int(c[10 - i])
                d = z*(11 - i -1)
                soma = soma + d
            x = soma % 11
            if x < 2:
                x = 0
            else:
                x = 11 - x
            soma = 0
            for i in range(0, 10):
                w = int(c[10 - i])
                d = w * (12 - i -1)
                soma = soma + d
            y = soma % 11
            if y < 2:
                y = 0
            else:
                y = 11 - y
            if int(c[1]) != x or int(c[0]) != y:
                print('*** CPF inválido')
            else:
                print('*** CPF válido \n>>>')
            print(c)
while True:
    VerificaCPF()