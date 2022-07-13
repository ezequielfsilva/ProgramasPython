num = int(input("Digite um número: "))
sn = "S"
count = 0
soma = 0
maior = menor = num
while sn == "S":
    count += 1
    soma += num
    sn = str(input("Quer continuar? [S/N] ")).upper().strip()
    if sn == "S":
        num = int(input("Digite um número: "))
    if maior < num:
        maior = num
    if menor > num:
        menor = num


print("Você digitou {} números e a média foi {}".format(count, soma/count))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))
