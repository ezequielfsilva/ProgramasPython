lanche = ('hamburguer', 'alface', 'salsicha', 'dog', 'pão')
x = len(lanche)
y = lanche[-3:-2]
z = sorted(lanche)
for i in range(0, len(lanche)):
    print(f'Eu comi a comida {lanche[i]} na posição {i}')
print(lanche[-4:])
print(x)
print(y)
print(z)