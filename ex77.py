lista = ('pao', 'leite', 'açucar', 'cafe', 'azeite', 'batata', 'iorgute', 'tempero', 'coxinha')
print(lista)
print('----'*20)
for i in lista:
    print(f'\nNa palavra {i.upper()} temos as vogais: ', end='')
    for j in i:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
            print(f'{j}', end=' ')




