lista = []
cont = maior = menor = 0
while True:
    lista.append(str(input('Digite um nome: ')))
    lista.append(int(input('Digite o peso: ')))
    resp = str(input("Quer continuar digitando? [S/N] ")).strip().upper()[0]
    cont += 1
    if resp == "N":
        break
for p in range(1, len(lista), 2):
    if p == 1:
        maior = lista[p]
        menor = lista[p]
        pes1 = lista[p-1]
        pes2 = lista[p-1]
    if lista[p] >= maior:
        maior = lista[p]
    if lista[p] <= menor:
        menor = lista[p]
print('-='*30)
print(f'{cont} pessoas foram cadastradas')
print(f'O maior peso digitado foi {maior}kg. Peso da(o)', end=' ')
for i in range(1, len(lista), 2):
    if lista[i] == maior:
        print(f'[{lista[i-1]}]', end=' ')
print(f'\nO menor peso digitado foi {menor}kg. Peso da(o)', end=' ')
for j in range(1, len(lista), 2):
    if lista[j] == menor:
        print(f'[{lista[j-1]}]', end=' ')