from datetime import date
ano = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - ano
print("O atleta tem {} anos".format(idade))
if idade <= 9:
    print("Categoria - MIRIM")
elif idade <= 14:
    print("Categoria - INFANTIL")
elif idade <= 19:
    print("Categoria - JUNIOR")
elif idade <= 25:
    print("Categoria - SÊNIOR")
else:
    print("Categoria - MASTER")
