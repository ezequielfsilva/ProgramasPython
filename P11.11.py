def main():
    '''
    Dado n > 0 inteiro,
    determinar o n-ésimo número primo.
    '''
    import math
    # ler n inteiro > 0
    n = int(input("Entre com o valor de n inteiro > 0: "))
    conta_primos = 0
    # Variar k a partir de 2 - não sabemos o limite superior
    k = 2
    while True:
        # Variar os candidatos a divisores de 2 até a raiz quadrada de k
        div = 2  # primeiro candidato a divisor
        for div in range(2, int(math.sqrt(k)) + 1):
            if k % div == 0:
                break  # sai do for
        # verifica se achou algum divisor ou saiu porque terminou o for
        else:
            # k é primo - incrementa 1 no contador de primos
            conta_primos += 1
            # chegou no n-ésimo número primo?
            if conta_primos == n:
                print("{} é o {}º primo".format(k, n))
                break  # sai do while e termina
        # testa o próximo candidato k
        k += 1


main()