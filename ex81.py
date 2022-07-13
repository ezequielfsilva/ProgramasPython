lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    sn = str(input('Quer continuar inserindo valores? [S/N] ')).strip().upper()[0]
    while sn != "S" and sn != "N":
        print("Digitação incorreta! Digite novamente.")
        sn = str(input('Quer continuar inserindo valores? [S/N] ')).strip().upper()[0]
    if sn == "N":
        break
print('-='*30)
lista.sort(reverse=True)
print(f'A quantidade de números digitados foi {len(lista)}')
print(f'Números digitados em ordem decrescente: {lista}')
print("O número 5 foi digitado e inserido na listagem" if 5 in lista else "O número 5 não foi digitado!")

