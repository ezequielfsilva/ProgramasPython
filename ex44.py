print("==="*10, end='')
print(" Lojas Sid ", end='')
print("==="*10)
preco = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO \n[1] à vista dinheiro/cheque \n[2] à vista cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão")
opcao = int(input("Qual é a opção? "))
if opcao == 1:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, preco*0.9))
elif opcao == 2:
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, preco * 0.95))
elif opcao == 3:
    parcelas = int(input("Quantas parcelas? "))
    print("Sua compra será parcelada em {}X de R${:.2f}".format(parcelas, preco/parcelas))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, preco))
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    valor = (preco*1.2)/parcelas
    print("Sua compra será parcelada em {}X de R${:.2f} COM JUROS".format(parcelas, valor))
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, preco * 1.2))
else:
    print("Opção INVÁLIDA de pagamento! Tente novamente.")
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(preco, preco))
