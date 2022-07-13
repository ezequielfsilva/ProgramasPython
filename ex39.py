from datetime import date

ano = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print("Quem nasceu em \033[1;32m{}\033[m tem \033[1;31m{}\033[m anos em \033[1;30m{}\033[m.".format(ano, idade, atual))

if idade > 18:
    print("Você já deveria ter se alistado há \033[1;33m{}\033[m anos!".format(idade - 18))
    print("Seu alistamento foi em \033[1;32m{}\033[m.".format(atual - idade + 18))
elif idade < 18:
    print("Ainda faltam \033[1;33m{}\033[m anos para o alistamento.".format(18 - idade))
    print("Seu alistamento será em \033[1;32m{}\033[m.".format(atual + 18 - idade))
else:
    print("Você tem que se alistar \033[1;33mIMEDIATAMENTE!\033[m")

