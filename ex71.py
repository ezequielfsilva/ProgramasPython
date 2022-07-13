print('---'*10)
print('      CAIXA ELETRÔNICO')
print('---'*10)
sacar = int(input('Qual valor você quer sacar? R$'))
total = sacar
ced50 = 50
totced = tot20 = tot10 = tot = 0
ced20 = 20
ced10 = 10
ced = 1
while True:
    if total >= ced50:
        total -= ced50
        totced += 1
    elif total >= ced20:
        total -= ced20
        tot20 += 1
    elif total >= ced10:
        total -= ced10
        tot10 += 1

    elif total >= ced:
        total -= ced
        tot += 1
    if total == 0:
        break
if totced >= 1:
    print(f'Total de {totced} cédulas de R${ced50}')
if tot20 >= 1:
    print(f'Total de {tot20} cédulas de R${ced20}')
if tot10 >= 1:
    print(f'Total de {tot10} cédulas de R${ced10}')
if tot >= 1:
    print('Total de {} cédulas de R${}'.format(tot, ced))
print('Volte sempre ao BANCO CITY. Tenha um bom dia.')
