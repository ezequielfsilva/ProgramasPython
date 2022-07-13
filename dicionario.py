pessoas = {'Nome': 'João', 'Idade': 29, 'Sexo': 'M'}
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
pessoas['Sexo'] = 'F'
pessoas['Peso'] = 70
del pessoas['Sexo']
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-=='*30)
brasil = []
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'São Luis', 'sigla': 'SL'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1]['uf'])