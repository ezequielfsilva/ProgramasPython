"""Programa simula um caixa eletrônico"""
print('* * * Dispensador de Notas * * *')
def verificador():
    while True:
        try:
            global n
            n = int(input('\nEntre com o valor em reais: '))
        except:
            print('Entrada inválida')

        else:
            if n % 10 != 0 and n > 0:
                print('* * * Erro * * * Valor tem que ser multiplo de 10')
            if n % 10 == 0 and n > 0:
                return n
                break
            if n <= 0:
                return n
                break

nota100 = 100
nota50 = 50
nota20 = 20
nota10 = 10
ced100 = ced50 = ced20 = ced10 = 0
x = y = z = w = 0
while True:
    verificador()
    if n <= 0:
        print('\n***Fim da operação***')
        break
    t = n
    while n >= nota100:
        ced100 += 1
        n -= 100
    while n >= nota50:
        ced50 += 1
        n -= 50
    while n >= nota20:
        ced20 += 1
        n -= 20
    while n >= nota10:
        ced10 += 1
        n -= 10
    while True:
        print('\nQuantidade de notas a serem sacadas:')
        if ced100 != 0:
            print(f'{ced100} nota(s) de 100')
        if ced50 != 0:
            print(f'{ced50} nota(s) de 50')
        if ced20 != 0:
            print(f'{ced20:.0f} nota(s) de 20')
        if ced10 != 0:
            print(f'{ced10:.0f} nota(s) de 10')
        m = str(input('\nDeseja sacar desta forma (s/n)? '))
        if m == 's':
            print('\n*Confirmado*')
            x += ced100
            y += ced50
            z += ced20
            w += ced10
            ced100 = 0
            ced50 = 0
            ced20 = 0
            ced10 = 0
            break
        a = ced100
        b = ced50
        c = ced20
        d = ced10
        if ced100 != 0:
            ced50 += 2 * ced100
            ced100 = 0
        if a == 0 and ced50 != 0:
            if ced50 % 2 == 0:
                ced20 += ced50 * 5 / 2
            elif ced50 % 2 == 1:
                ced20 += (ced50 * 50 - 10) / 20
                ced10 += 1
            ced50 = 0
        if a == 0 and b == 0 and ced20 != 0:
            ced10 += 2 * ced20
            ced20 = 0
        if a == 0 and b == 0 and c == 0 and m == 'n':
            print('*Nenhuma opção foi aceita*')
            ced10 = 0
            n = t
            break
print('\nTotal de notas sacadas:')
print(f' {x} nota(s) de 100')
print(f' {y} nota(s) de 50')
print(f' {z:.0f} nota(s) de 20')
print(f' {w:.0f} nota(s) de 10')
t = x * 100 + y * 50 + z * 20 + w * 10
print(f'\n Valor total: {t:.0f} reais')
