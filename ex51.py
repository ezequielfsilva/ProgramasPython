primeiro = int( input("Prinmeiro termo: "))
razao = int( input("Razão: "))
decimo = primeiro + (10 -1)*razao
for i in range(primeiro, decimo + razao, razao):
    print("{}".format(i), end=" ¬ ")
print("Acabou!")