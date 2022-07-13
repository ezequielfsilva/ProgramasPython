distancia = float(input("\033[1;33mQual é a distância da sua viagem (em KM)? \033[m"))
print("Você está prestes a começar uma viagem de {}KM.".format(distancia))
if distancia > 200:
    preco = distancia*0.45

else:
    preco = distancia*0.5

print("E o preço da sua passagem será de \033[1;31mR${:.2f}\033[m".format(preco))