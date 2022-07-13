lista = [3, 4, 7, 9, 1]
a = [3, 6, 0]
b = a[:]
b[0] = -8
lista.append(2)
lista.sort(reverse=True)
lista.insert(1, -5)
lista.pop(0)
print(lista)
print(a)
print(b)
