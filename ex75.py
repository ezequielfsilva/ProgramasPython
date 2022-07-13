lista = (int(input("Digite um número: ")),
         int(input("Digite um número: ")),
         int(input("Digite um número: ")),
         int(input("Digite um número: ")))
x = 0
print(f"Você digitou os valores {lista}")
print(f'O número 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)+1} posição')
else:
    print("O número 3 não foi digitado em nenhuma posição")
print('Os valores pares digitados foram: ', end='')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        x += 1

print("{}".format('NENHUM' if x == 4 else ''))
