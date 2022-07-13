print("---"*20)
print("    LOJA SUPER BARATÃO")
print("---"*20)
soma = quanti = quanti1 = 0
while True:
    produto = str(input("Nome do Produto: ")).strip()
    preco = float(input("Preço: R$"))
    soma += preco
    quanti += 1
    if quanti == 1:
        barato = preco
        bp = produto
    if barato > preco:
        barato = preco
        bp = produto
    if preco > 1000:
        quanti1 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
        break
print("----"*5, "FIM DO PROGRAMA", "----"*5)
print("O total da compra foi R${:.2f}".format(soma))
print("Temos {} produtos custando mais de R$1000.00".format(quanti1))
print("O produto mais barato foi {} que custa R${:.2f}".format(bp, barato))
