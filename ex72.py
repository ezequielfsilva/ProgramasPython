cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    while num < 0 or num > 20:
        num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"\033[1;32m{cont[num]}\033[m foi o número que você digitou")
    print('-=='*15)
    sn = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if 0 <= num <= 20 and sn == 'N':
        break
print("Fim do programa")