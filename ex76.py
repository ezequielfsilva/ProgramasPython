produtos = ('pão', 8.99, 'carne', 25.00, 'pizza', 39.99, 'lasanha', 28.99, 'batata', 2.99, 'tomate', 5.99)
print('--'*15)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('--'*15)
for i in range(0, 12, 2):
    d = len(produtos[i])
    z = '.'*(21 - d)
    print("{} {} R${:5.2f}".format(produtos[i], z, produtos[i+1]))
print('--'*15)