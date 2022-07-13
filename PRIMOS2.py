par, par1, par2 = '', '', ''
impar, impar1, impar2 = '', '', ''
for i in range(255, 1000):
    if i % 2 == 0:
        par = 18 * (i / 2 - 1) + 11
        par1 = 18*(i/2-1)+13
        par2 = 18 * (i / 2 - 1) + 17
        print('{:.0f}'.format(par))
        print('{:.0f}'.format(par1))
        print('{:.0f}'.format(par2))
        del par, par1, par2
    else:
        impar = 18 * ((i + 1) / 2 - 1) + 1
        impar1 = 18*((i+1)/2 - 1) + 5
        impar2 = 18 * ((i + 1) / 2 - 1) + 7
        print('{:.0f}'.format(impar))
        print('{:.0f}'.format(impar1))
        print('{:.0f}'.format(impar2))
        del impar, impar1, impar2