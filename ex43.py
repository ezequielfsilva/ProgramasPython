
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em m): "))
imc = peso/(altura**2)
if imc < 18.5:
    print("Seu imc é \033[1;31m{:.2f}\033[m. Você está \033[1;32mabaixo do peso\033[m.".format(imc))
elif imc < 25:
    print("Seu imc é \033[1;31m{:.2f}\033[m. Você está no \033[1;32mpeso ideal\033[m.".format(imc))
elif imc < 30:
    print("Seu imc é \033[1;31m{:.2f}\033[m. Você está com \033[1;32msobrepeso\033[m.".format(imc))
elif imc < 40:
    print("Seu imc é \033[1;31m{:.2f}\033[m. Você está com \033[1;32mobesidade\033[m.".format(imc))
else:
    print("Seu imc é \033[1;31m{:.2f}\033[m. Você está com \033[1;32mobesidade mórbida\033[m.".format(imc))
