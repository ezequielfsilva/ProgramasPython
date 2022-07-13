def main():
     '''
     Dado n > 0, calcular e imprimir os n primeiros primos.
     Lembrando que um número é primo, se não tem divisores entre 2 e raiz
    de n
     '''
     import math

     # ler n inteiro >= 1
     n = int(input("Entre com o valor de n inteiro > 0: "))
     conta_primos = 0
     # Variar k a partir de 2 - não sabemos o limite superior
     k = 2
     while True:

         # Variar os candidatos a divisores de 2 até a raiz quadrada de k
         div = 2 # primeiro candidato a divisor
         for div in range(2, int(math.sqrt(k)) + 1):
            if k % div == 0:
                break # sai do for
         # verifica se achou algum divisor ou saiu porque terminou o for
         else:
         # k é primo - incrementa 1 no contador de primos e imprime
             conta_primos += 1
             print(k, "é o primo de ordem", conta_primos)
             # chegou no n-ésimo número primo?
             if conta_primos == n:
                print("acima estão os", n, "primeiros primos")
                break # sai do while e termina
         # testa o próximo candidato k
         k += 1
main()