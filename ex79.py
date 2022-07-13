lista = []
while True:
    lista.append(int(input("Digite um valor: ")))
    for i, c in enumerate(lista):
        for j, d in enumerate(lista):
            if c == d and i != j:
                lista.pop(i)
                print("Valor repetido! NÃO SERÁ ADICIONADO.")
    while True:
        conti = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if conti in 'SN':
            break
        print("Você digitou incorretamente!\nDigite novamente.")
    if conti == 'N':
        break
lista.sort()
print('-==-'*20)
print(f'Esses foram os valores adicionados em ordem crescente: {lista}')