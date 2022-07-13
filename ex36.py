casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento: "))

prestacao = casa / (12*anos)
print("Para pagar uma casa no valor R${:.2f} em {} anos a prestação será de R${:.2f} mensais.".format(casa, anos, prestacao))
if prestacao > (0.3*salario):

    print("Empréstimo NEGADO!")
else:
    print("Empréstimo CONCEDIDO!")
