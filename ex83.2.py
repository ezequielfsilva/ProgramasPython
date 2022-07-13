n = str(input('Digite uma expressão com uso de parenteses (): ')).strip()
pilha = []
for i in range(0, len(n)):
    if n[i] == '(':
        pilha.append('(')
    if n[i] == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida.')
else:
    print("Sua expressão está errada!")
