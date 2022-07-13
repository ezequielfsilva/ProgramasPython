count = soma = 0
while True:
    num = int(input("Digite um número ou 999 para parar: "))
    if num == 999:
        break
    count += 1
    soma += num
print("A soma dos {} valores foi {}".format(count, soma))
