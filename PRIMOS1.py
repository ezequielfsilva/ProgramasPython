par = ''
impar = ''
for i in range(1, 10):
    if i % 2 == 0:
        par = 16*(i/2-1)+13
        print('{:.0f}'.format(par))

    else:
        impar = 16*((i+1)/2 - 1) + 5
        print('{:.0f}'.format(impar))
