list = []
for i in range(1, 6):
    peso = float(input("Peso da {}ª pessoa: kg".format(i)))
    list += [peso]
print(list)
for i in range(0, 5):
        if list[i] >= list[0] and list[i] >= list[1] and list[i] >= list[2] and list[i] >= list[3] and list[i] >= list[4]:
            print("O \033[1;34mMAIOR\033[m peso lido foi \033[1;34m{}\033[mkg".format(list[i]))
        if list[i] <= list[0] and list[i] <= list[1] and list[i] <= list[2] and list[i] <= list[3] and list[i] <= list[4]:
            print("O \033[1;31mMENOR\033[m peso lido foi \033[1;31m{}\033[mkg".format(list[i]))


