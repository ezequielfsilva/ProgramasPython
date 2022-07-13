numero = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:")
print("[1] converter para BINÁRIO.")
print("[2] converter para OCTAL.")
print("[3] converter para HEXADECIMAL.")
n = int(input("Sua opção: "))
if n == 1:
    print("{} convertido para BINÁRIO é {}".format(numero, bin(numero)[2:]))
if n == 2:
    print("{} convertido para OCTAL é {}".format(numero, oct(numero)[2:]))
if n == 3:
    print("{} convertido para HEXADECIMAL é {}".format(numero, hex(numero)[2:]))
else:
    print("Opção inválida. Tente novamente.")

