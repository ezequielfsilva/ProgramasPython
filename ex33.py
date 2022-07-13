p1 = int(input("\033[1;31mPrimeiro número: \033[m"))
p2 = int(input("\033[1;32mSegundo número: \033[m"))
p3 = int(input("\033[1;33mTerceiro número: \033[m"))

##posso economizar um 'if', tanto na condição maior como na menor,
## utilizando a variável 'menor\maior' já recebendo um dos valores digitados.

if p1 < p2 and p1 < p3:
    menor = p1
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p1 and p3 < p2:
    menor = p3

if p1 > p2 and p1 > p3:
    maior = p1
if p2 > p1 and p2 > p3:
    maior = p2
if p3 > p1 and p3 > p2:
    maior = p3

print("O menor número digitado é o \033[1;34m{}\033[m.".format(menor))
print("O maior número digitado é o \033[1;35m{}\033[m.".format(maior))