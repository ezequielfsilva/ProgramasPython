n = int(input("Digite um número ou 999 para parar: "))
soma = quantidade =0
while n != 999:
    soma += n
    quantidade += 1
    n = int(input("Digite um número entre 0 e 999 ou 999 para parar: "))

print("{} foi a quantidade de números digitados e {} foi a soma.".format(quantidade, soma))