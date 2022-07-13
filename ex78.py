valores = []
maior = ''
menor = ''
d = ''
h = ''
for i in range(0, 5):
    valores.append(int(input(f"Digite um número para a posição {i}: ")))
for pos, j in enumerate(valores):
    if pos == 0:
        maior = j
        menor = j
        d = pos
        h = pos
    if j > maior:
        maior = j
        d = pos
    if j < menor:
        menor = j
        h = pos
print(valores)
print(f'O maior valor digitado da lista foi {maior} nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}ª...', end='')
print(f'\nO menor valor digitado da lista foi {menor} nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}ª...', end='')