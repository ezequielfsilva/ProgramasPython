quantidade = 0
soma = 0
for i in range(3,500, 6):
    soma = soma + i
    quantidade += 1
print("A soma de todos os {} valores solicitados é {}".format(quantidade, soma))
