cont = ('corinthians','santos','pl','sp','int','gre','fla',
        'flu','vas','bot','cru','atl','ath','goias',
        'chapecoense','avai','for','bahia','sport','ceara')

print(f'Lista de timres: {cont}')
print('-=='*15)
print(f'Os 4 primeiros são: {cont[0:4]}')
print('-=='*15)
print(f'Os 4 últimos são: {cont[-4:]}')
print('-=='*15)
print(f'Lista de times em ordem alfabética: {sorted(cont)}')
print('-=='*15)
print(f'A chapecoense está na posição {cont.index("chapecoense")+1}ª')
