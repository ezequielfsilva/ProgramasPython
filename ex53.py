
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

###Sem a função '[::-1}' temos que utilizar o FOR

'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''


print("O inverso de {} é {}".format(junto, inverso))
if junto == inverso:
    print("Temos um PALÍNDROMO")
else:
    print("A frase digitada NÃO É UM PALÍNDROMO!")


