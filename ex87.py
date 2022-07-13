matrix = [[], [], []]
cont = contcoluna = 0
maior = ''
for i in range(0, 3):
    for j in range(0,3):
        n = int(input('Digite um valor: '))
        matrix[i].append(n)
        if n % 2 == 0:
            cont += n
        if j == 2:
            contcoluna += matrix[i][j]
        if i == 1:
            if j == 0:
                maior = matrix[i][j]
            elif matrix[i][j] > maior:
                maior = matrix[i][j]
print('-='*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[i][j]:^5}]', end=' ')
    print()
print('-='*30)
print(f'A soma de todos os números PARES digitados foi: {cont}')
print(f'A soma dos números na terceira coluna é {contcoluna}')
print(f'O maior valor da segunda linha é {maior}')