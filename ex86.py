matrix = [[], [], []]
for j in range(0, 3):
    for i in range(0, 3):
        n = int(input(f'Digite um número para a posição {[j+1,i+1]} da matrix: '))
        matrix[j].append(n)
print(matrix)
for k in range(0, 3):
    for j in range(0, 3):
        print(f'[{matrix[k][j]:^5}]', end=' ')
    print()