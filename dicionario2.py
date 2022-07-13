estado = {}
brasil = []
for i in range(0, 3):
    estado['uf'] = str(input('Digite uma cidade: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for i in e:
        print(i, end=' ')
    print()