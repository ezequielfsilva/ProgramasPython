print("       GERADOR DE PA")
print("=-=="*8)
print("       10 primeros termos da PA")
print("=-=="*8)
pt = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
i = 1
while i <= 10:
    print("A{} = {}".format(i, pt), end=", ")
    pt += razao
    i += 1
print("\nAcabou o programa!")
