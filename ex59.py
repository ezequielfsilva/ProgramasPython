from time import sleep
n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input(">>>>> Qual a sua opção? "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma entre {} e {} é {}".format(n1, n2, soma))
    elif opcao == 2:
        multi = n1*n2
        print("A multiplicação entre {} e {} é {}".format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            print("Entre {} e {} o maior é {}".format(n1, n2, n1))
        elif n1 < n2:
            print("Entre {} e {} o maior é {}".format(n2, n1, n2))
        else:
            print("São iguais")
    elif opcao == 4:
        print("DIGITE NOVOS NÚMEROS")
        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))
    elif opcao == 5:
        print("Finalizando...")
    elif opcao >= 6:
        print("Você digitou uma opção inválida! \nDigite novamente uma opão entre as estabelecidas no menu.")
    print("=-=="*15)
    sleep(2)
print("Fim do programa! Volte sempre.")


