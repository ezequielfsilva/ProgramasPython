num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print("{} X {:2} = {}".format(num, i, num*i))
