n = str(input('Digite uma expressão com uso de parenteses (): ')).strip()
x = 0
y = 0
for i in range(0, len(n)):
    if n[i] == '(':
        x += 1
    if n[i] == ')':
        y += 1
if x == y:
    print('Sua expressão está válida.')
elif x != y:
    print("Sua expressão está errada!")
