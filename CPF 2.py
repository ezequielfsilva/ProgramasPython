"""Verifica se um CPF digitado é válido ou não"""
def VerificaCPF():
    m = str(input('Entre com um CPF: '))
    try:
        int(m)
    except:
        print('*** CPF inválido')
    else:
        if len(m) != 11:
            print('*** CPF inválido')
        else:
            b = list(m)
            soma = 0
            for i in range(0, 9):
                z = int(b[i])
                d = z * (11 - i -1)
                soma = soma + d
            x = soma % 11
            if x < 2:
                x = 0
            else:
                x = 11 - x
            soma = 0
            for i in range(0, 10):
                w = int(b[i])
                d = w * (12 - i -1)
                soma = soma + d
            y = soma % 11
            if y < 2:
                y = 0
            else:
                y = 11 - y
            if int(b[9]) != x or int(b[10]) != y:
                print('*** CPF inválido')
            else:
                print('*** CPF válido \n>>>')
while True:
    VerificaCPF()
