from datetime import date
quantidade = 0
quantidade2 = 0
for i in range(1, 8):
    ano = int(input("Em que ano a {}ª pessoa nasceu? ".format(i)))
    idade = date.today().year - ano
    if idade >= 21:
        quantidade += 1
    else:
        quantidade2 += 1
print("Ao todo tivemos {} pessoas maiores de idade. \nE também tivemos {} pessoas menores de idade.".format(quantidade, quantidade2))
