for i in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: kg".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O \033[1;34mMAIOR\033[m peso lido foi \033[1;34m{}\033[mkg".format(maior))
print("O \033[1;31mMENOR\033[m peso lido foi \033[1;31m{}\033[mkg".format(menor))
