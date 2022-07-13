i = int(input("Quantos termos vc quer da sequencia de Fibonacci: "))
j = 0
x1 = 0
x2 = 1
while j <= i - 1:
    if j <= 1:
        print("{}".format(j), end=' ¬¬ ')
    else:
        x = x1 + x2
        print("{}".format(x), end=' ¬¬ ')
        x1 = x2
        x2 = x
    j += 1
print("\nAcabou o programa!")
