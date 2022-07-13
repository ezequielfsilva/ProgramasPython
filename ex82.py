lista = []
lista1 = []
lista2 = []
while True:
    lista.append(int(input("Digite um valor: ")))
    sn = str(input("Quer continuar digitando? [S/N] ")).strip().upper()[0]
    while sn != "S" and sn!= "N":
        print("Digitação incorreta! Digite novamente.")
        sn = str(input("Quer continuar digitando? [S/N] ")).strip().upper()[0]
    if sn == "N":
        break
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        lista1.append(lista[i])
    else:
        lista2.append(lista[i])
print('-='*30)
print(f'Esses foram os valores digitados: {lista}')
print(f'Esses foram os valores PARES digitados: {lista1}')
print(f'Esses foram os valores ÍMPARES digitados: {lista2}')