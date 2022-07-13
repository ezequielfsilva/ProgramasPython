"""Olá. Esse programa calcula os valores das funções SENO e COSSENO através da Série de Taylor."""
import math
import time

print('Olá. Esse programa calcula os valores das funções SENO e COSSENO através da Série de Taylor.')
print('Você precisará inserir o valor de x para o qual as funções serão calculadas'
      'e também a quantidade (n) de termos para a Série de Taylor \n')
time.sleep(0.5)


def seno(entradaX, quantidadeN):
    # CÁLCULO DO SENO PELA SÉRIE DE TAYLOR
    soma, fat, pot = 0, 1, entradaX
    for i in range(1, 2 * quantidadeN, 2):
        soma = soma + pot / fat
        pot = -pot * entradaX * entradaX
        fat = fat * (i + 1) * (i + 2)
    return soma  # RETORNA PARA QUEM CHAMOU A FUNÇÃO O VALOR DA VÁRIÁVEL 'soma'


def cosseno(entradaX, quantidadeN):
    # CÁLCULO DO COSSENO PELA SÉRIE DE TAYLOR
    soma2, fat, pot = 0, 1, 1
    for i in range(0, 2 * quantidadeN, 2):
        soma2 = soma2 + pot / fat
        pot = -pot * entradaX * entradaX
        fat = fat * (i + 1) * (i + 2)
    return soma2  # RETORNA PARA QUEM CHAMOU A FUNÇÃO O VALOR DA VÁRIÁVEL 'soma2'


cont = 0  # 'cont' AJUDA NA SAÍDA DO PROGRAMA, EM SEUS COMANDOS E QUANDO VALE 'ZERO' É O INÍCIO DO PROGRAMA
while True:
    if cont == 1:
        # PERGUNTA AO USUÁRIO SE DESEJA CONTINUAR NO PROGRAMA SE 'cont == 1'
        continuar = input('Deseja continuar? [S/N] ').upper()
        if len(continuar) == 1 and continuar == 'N':
            break  # ENCERRAR O PROGRAMA E SAIR
        elif len(continuar) != 1:
            print("ERRO!! Entrada inválida. Digite 'S' ou 'N'")
            continue
        elif len(continuar) == 1 and continuar != 'S' and continuar != 'N':
            print("ERRO!! Entrada inválida. Digite 'S' ou 'N'")
            continue
        elif len(continuar) == 1 and continuar == 'S':
            print()
            # CONTINUAR EXECUTANDO O PROGRAMA

    cont2 = 0  # VARIÁVEL QUE QUANDO RECEBE O VALOR '1' AJUDA A DESIGINAR PARA AS VARIÁVEIS 'entradaX' E 'quantidadeN'
    #  OS ANTIGOS VALORES DESSAS VARIÁVEIS - (QUANDO O USUÁRIO NÃO DIGITA NADA PARA ELAS - SIMPLESMENTE DA 'ENTER')
    while True:
        if cont2 == 1:
            entradaX = antigovalorX  # 'entradaX' RECEBENDO O SEU ANTIGO VALOR DIGITADO ('antigovalorX')
            cont2 = 0  # ZERAR A VARIÁVEL DE NOVO PARA RECOMEÇAR O PROCESSO
        else:
            entradaX = input('Entre com o x: ')  # PEDINDO AO USUÁRIO QUE DIGITE UM VALOR PARA 'entradaX'

        try:
            entradaX = float(entradaX)  # VERIFICANDO SE O QUE FOI DIGITADO PARA A 'entradaX' É UM 'FLOAT'
            antigovalorX = entradaX  # 'antigovalorX' RECEBENDO O VALOR ATUAL DA VARIÁVEL 'entradaX' P/ SER USADA
            #  POSTERIORMENTE QUANDO 'cont2 == 1' E NA APRESENTAÇÃO FINAL AO USUÁRIO
            entradaX = entradaX % (2 * math.pi)  # TRANSFORMANDO O QUE O USUÁRIO DIGITOU NUM VALOR ENTRE 0 E 2*MATH.PI
        except:
            if cont == 1:
                # VERIFICANDO SE NÃO FOI DIGITADO NADA PARA A VARIÁVEL 'entradaX'
                # (QUANDO O USUÁRIO DAR 'ENTER' SEM DIGITAR NADA)
                if len(entradaX) == 0:
                    cont2 = 1  # COMANDO PARA DESIGNAR A 'entradaX' SEU ANTIGO VALOR ('antigovalorX')
                    continue
            print('>>>>> ERRO!! Entrada inválida.')
            continue
        else:
            while True:
                if cont2 == 1:
                    quantidadeN = antigovalorN  # 'quantidadeN' RECEBENDO O SEU ANTIGO VALOR DIGITADO ('antigovalorN')
                    cont2 = 0  # ZERAR A VARIÁVEL DE NOVO PARA RECOMEÇAR O PROCESSO
                else:
                    # PEDINDO AO USUÁRIO QUE DIGITE UM VALOR PARA 'quantidadeN'
                    quantidadeN = input('Entre com o valor de n inteiro no intervalo de 1 a 50: ')
                try:
                    quantidadeN = int(quantidadeN)  # VERIFICANDO SE O QUE FOI DIGITADO É UM 'INTEIRO'
                    # FAZENDO A CONSISTÊNCIA P/ VERIFICAR SE ESTÁ NO INTERVALO INDICADO
                    if quantidadeN <= 0 or quantidadeN >= 51:
                        print('>>>>> ERRO!! Inteiro digitado fora do intervalo permitido [1, 50].')
                        continue
                    # 'antigovalorN' RECEBENDO O VALOR ATUAL DA VARIÁVEL 'quantidadeN'
                    # PARA SER USADA POSTERIORMENTE QUANDO 'cont2 == 1' E NA APRESENTAÇÃO FINAL AO USUÁRIO
                    antigovalorN = quantidadeN
                except:
                    if cont == 1:
                        # VERIFICANDO SE NÃO FOI DIGITADO NADA PARA A VARIÁVEL 'quantidadeN'
                        # (QUANDO O USUÁRIO DAR 'ENTER' SEM DIGITAR NADA)
                        if len(quantidadeN) == 0:
                            cont2 = 1  # COMANDO PARA DESIGNAR A VARIÁVEL 'quantidadeN' SEU ANTIGO VALOR ('antigovalorN')
                            continue
                    print('>>>>> ERRO!! Entrada inválida.')
                else:
                    # SE CHEGAR ATÉ AQUI, ENCERRAR O 'WHILE TRUE' DA VARIÁVEL 'quantidadeN'
                    break
        # SE CHEGAR ATÉ AQUI, ENCERRAR O 'WHILE TRUE' DA VARIÁVEL 'entradaX'
        break
    from time import process_time

    t = process_time()  # VALOR ATUAL DO RELÓGIO
    serietaylor = seno(entradaX, quantidadeN)  # CÁLCULO A SER FEITO PELA SÉRIE DE TAYLOR - SENO
    dt = process_time() - t  # TEMPO DE PROCESSAMENTO DECORRIDO PARA O CÁLCULO
    t2 = process_time()  # VALOR ATUAL DO RELÓGIO
    senoX = math.sin(entradaX)  # FUNÇÃO SENO SENDO CÁCULADA PELA FUNÇÃO MATH.SIN
    dt2 = process_time() - t2  # TEMPO DE PROCESSAMENTO DECORRIDO PARA O CÁLCULO
    t3 = process_time()  # VALOR ATUAL DO RELÓGIO
    serietaylor2 = cosseno(entradaX, quantidadeN)  # CÁLCULO A SER FEITO PELA SÉRIE DE TAYLOR - COSSENO
    dt3 = process_time() - t3  # TEMPO DE PROCESSAMENTO DECORRIDO PARA O CÁLCULO
    t4 = process_time()  # VALOR ATUAL DO RELÓGIO
    cossenoX = math.cos(entradaX)  # FUNÇÃO COSSENO SENDO CÁCULADA PELA FUNÇÃO MATH.COS
    dt4 = process_time() - t4  # TEMPO DE PROCESSAMENTO DECORRIDO PARA O CÁLCULO
    cont = 1  # VARIÁVEL 'cont' RECEBENDO 1 PARA DIFERENCIAR DA PRIMEIRA VEZ QUE O PROGRAMA RODAR
    # PRINTS PARA MOSTRAR AO USUÁRIO OS CÁLCULOS DA SERIES DE TAYLOR PARA O SENO E O COSSENO
    print('\nValores calculados para:')
    print('x =', antigovalorX, '\nn =', quantidadeN)
    print('\nSeno:')
    print('Usando a soma de termos: {}  -  tempo: {}'.format(serietaylor, dt))
    print('Usando a função Seno:    {}  -  tempo: {}'.format(senoX, dt2))
    print('\nCosseno:')
    print('Usando a soma de termos: {}  -  tempo: {}'.format(serietaylor2, dt3))
    print('Usando a função Cosseno: {}  -  tempo: {}'.format(cossenoX, dt4))
    print('\n* * * * * * * * *')
    print()
