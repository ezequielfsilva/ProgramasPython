num = int(input("Digite um número: "))
quant = 0
for i in range(1, num+1):
        if num % i == 0:
            quant += 1
            print("\033[1;33m{}\033[m".format(i), end=" ")
        else:
            print("\033[1;31m{}\033[m".format(i), end=" ")
if quant != 2:
    print("\nO numero {} foi dividido {} vezes. \nE por isso \033[0;35mNÃO É PRIMO!\033[m".format(num, quant))
else:
    print("\nO número {} foi dividido {} vezes. \nE por isso ele \033[0;34mÉ PRIMO!\033[m".format(num, quant))
