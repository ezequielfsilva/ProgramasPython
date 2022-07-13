n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))

if n1 > n2:
    print("O PRIMEIRO número que é {} é maior que o SEGUNDO número que é {}".format(n1, n2))
elif n2 > n1:
    print("O SEGUNDO número que é {} é maior que o PRIMEIRO número que é {}".format(n2, n1))
else:
    print("Os dois valores são IGUAIS")
