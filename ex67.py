while True:
    num = int(input("Digite um número para ver sua Tabuada: "))
    if num < 0:
        break
    for i in range(1, 11):
        print("{} x {:2} = {:2}".format(num, i, num*i))
print("Programa tabuada encerrado! Volte sempre.")