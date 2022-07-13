quantim = 0
quantI = 0
maisvelho = 0
for i in range(1, 5):
    print("---------- {}ª pessoa ----------".format(i))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    quantI += idade
    if sexo == "M" and idade > maisvelho:
        maisvelho = idade
        nome1 = nome
    if sexo == "F" and idade < 20:
        quantim += 1
print("A média de idade do grupo é de {} anos".format(quantI/4))
print("O homem mais velho tem {} anos e se chama {}".format(maisvelho, nome1))
print("Ao todo são {} mulheres com menos de 20 anos".format(quantim))