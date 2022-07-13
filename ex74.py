from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(num)
print('-=='*15)
print(f'O maior valor escolhido foi {max(num)}')
print('-=='*15)
print(f'O menor valor escolhido foi {min(num)}')
