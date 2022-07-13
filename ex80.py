lista = []
for i in range(0, 5):
    lista.append(int(input("Digite um valor: ")))
    if i == 0:
        print('Adicionado na posição 0...')
    if i == 1:
        if lista[0] > lista[1]:
            aux = lista[0]
            lista[0] = lista[1]
            lista[1] = aux
            print('adicionado na posição {} da lista...'.format(0))
        else:
            print('Adicionado no final da lista...')
    if i >= 2:
        g = 0
        for k in range(0, i+1):
            if lista[i] >= lista[k]:
                g += 1
        if g == k+1:
            print('Adicionado no final da lista...')
        for j in range(0, i+1):
            if lista[i] < lista[j]:
                lista.insert(j, lista[i])
                lista.pop(i+1)
                if lista[i] > lista[j]:
                    print(f'Adicionado na posição {j} da lista...')
print('=#='*15)
print(lista)