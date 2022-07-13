par = ''
impar = ''
for i in range(1, 100):
    if i % 2 == 0:
        par = 18*(i/2-1)+13
        if par % 5 != 0 and par % 7 != 0 and par % 11 != 0 and par % 13 != 0 and par % 17 != 0 and par % 19 != 0 and par % 23 != 0 and par % 29 != 0 and par % 31 != 0:
            print('{:.0f}'.format(par))
        elif par == 5 or par == 7 or par == 11 or par == 13 or par == 17 or par == 19 or par == 23 or par == 29 or par == 31:
            print('{:.0f}'.format(par))
        del par
    else:
        impar = 18*((i+1)/2 - 1) + 5
        if impar % 5 != 0 and impar % 7 != 0 and impar % 11 != 0 and impar % 13 != 0 and impar % 17 != 0 and impar % 19 != 0 and impar % 23 != 0 and impar % 29 != 0 and impar % 31 != 0:
            print('{:.0f}'.format(impar))
        elif impar == 5 or impar == 7 or impar == 11 or impar == 13 or impar == 17 or impar == 19 or impar == 23 or impar == 29 or impar == 31:
            print('{:.0f}'.format(impar))
        del impar
