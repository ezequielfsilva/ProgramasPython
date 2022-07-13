numero = int(input("\033[1;33mDigite um número: \033[m"))
if numero % 2 == 0:
    print("O número {} é par.".format(numero))
else:
    print("O número {} é impar.".format(numero))