from random import randint
print("\033[1;35mSou seu computador...\033[m")
print("\033[1;34mAcabei de pensar em um número entre 0 e 10\033[m")
print("\033[1;33mSerá que você consegue adivinhar qual foi?\033[m")
jogador = int(input("\033[0;31mQual seu palpite?\033[m "))
quantidade = 1
computador = randint(0, 10)
while jogador != computador:
    if jogador > computador:
        print("Menos... Tente outra vez.")
    if jogador < computador:
        print("Mais... Tente outra vez.")
    quantidade += 1
    jogador = int(input("\033[0;31mQual seu palpite?\033[m "))

print("Acertou com \033[1;33m{}\033[m tentativas. Parabéns!".format(quantidade))