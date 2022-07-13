quanti1 = count = quanti = 0
while True:
    print('--' * 15)
    print("     CADASTRE UMA PESSOA")
    print('--' * 15)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    print('--' * 15)
    if idade > 18:
        count += 1
    if sexo == "M":
        quanti += 1
    elif idade < 20:
        quanti1 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        break
print("Total de pessoas com mais de 18 anos: {}".format(count))
print("Ao todo temos {} homens cadastrados".format(quanti))
print("E temos {} mulheres com menos de 20 anos".format(quanti1))
