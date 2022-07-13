## Pode ser feito desse jeito
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
n4 = int(input("Quarto número: "))
n5 = int(input("Quinto número: "))
n6 = int(input("Sexto número: "))
list = [n1, n2, n3, n4, n5, n6]
print(list)
soma = 0

for i in list:
    if i % 2 == 0:
        soma += i

print(soma)

## Como pode ser feito desse jeito
soma1 = 0
quant = 0
for i in range(1,7):
    num = int(input("Digite o {} valor".format(i)))
    if num % 2 == 0:
        soma1 += num
        quant += 1
print("Você informou {} números PARES e a soma foi {}".format(quant, soma1))
