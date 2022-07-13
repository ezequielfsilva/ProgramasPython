import math
import time
print('Olá. Esse programa calcula o valor da função EXPONENCIAL (e*x) através da Série de Taylor.')
print('Você precisará inserir o valor de x para o qual a função será calculada e também o valor do epsylon (eps) '
      'como parâmetro para a Série de Taylor \n')
time.sleep(0.5)
def exp(entradaX, eps):
    # CÁLCULO DA EXPONENCIAL PELA SÉRIE DE TAYLOR
    soma, i, fat, pot = 1, 1, 1, entradaX
    while True:
        termoserie = pot / fat
        soma = soma + termoserie
        pot = pot * entradaX
        fat = fat * (i + 1)
        i += 1
        if math.fabs(eps) >= math.fabs(termoserie):
            break
    return soma  # RETORNA PARA QUEM CHAMOU A FUNÇÃO O VALOR DA VÁRIÁVEL 'soma'

cont = 0  # ELA AJUDA NA SAÍDA DO PROGRAMA, EM SEUS COMANDOS E QUANDO VALE 'ZERO' É O INÍCIO DO PROGRAMA
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

    cont2 = 0  # É UMA VARIÁVEL QUE QUANDO RECEBE O VALOR '1' AJUDA A DESIGNAR PARA AS VARIÁVEIS 'entradaX' E 'eps'
    # OS ANTIGOS VALORES DESSAS VARIÁVEIS (QUANDO O USUÁRIO NÃO DIGITA NADA PARA ELAS - SIMPLESMENTE DA 'ENTER')
    while True:
        if cont2 == 1:
            entradaX = antigovalorX  # 'entradaX' RECEBENDO O SEU ANTIGO VALOR DIGITADO ('antigovalorX')
            cont2 = 0  # ZERAR A VARIÁVEL 'cont2' PARA RECOMEÇAR O PROCESSO
        else:
            entradaX = input('Entre com o x: ')  # PEDINDO AO USUÁRIO QUE DIGITE UM VALOR PARA 'entradaX'
        try:
            entradaX = float(entradaX)  # VERIFICANDO SE O QUE FOI DIGITADO PARA A 'entradaX' É UM 'FLOAT'
            if entradaX > 10 or entradaX < -10:
                print('ERRO!! Fora do intervalo permitido.')
                continue
            antigovalorX = entradaX  # VARIÁVEL 'antigovalorX' RECEBENDO O VALOR ATUAL DA VARIÁVEL 'entradaX'
            # PARA SER USADA POSTERIORMENTE QUANDO 'cont2 == 1' E NA APRESENTAÇÃO FINAL AO USUÁRIO
        except:
            if cont == 1:
                if len(entradaX) == 0:  # VERIFICANDO SE NÃO FOI DIGITADO NADA PARA A VARIÁVEL 'entradaX'
                                        # (QUANDO O USUÁRIO DAR 'ENTER' SEM DIGITAR NADA)
                    cont2 = 1  # COMANDO PARA DESIGNAR A 'entradaX' SEU ANTIGO VALOR ('antigovalorX')
                    continue
            print('>>>>> ERRO!! Entrada inválida.')
            continue
        else:
            while True:
                if cont2 == 1:
                    eps = antigovalorEPS  # VARIÁVEL 'eps' RECEBENDO O SEU ANTIGO VALOR DIGITADO ('antigovalorEPS')
                    cont2 = 0  # ZERAR A VARIÁVEL 'cont2' PARA RECOMEÇAR O PROCESSO
                else:
                    # PEDINDO AO USUÁRIO QUE DIGITE UM VALOR PARA 'eps'
                    eps = input('Entre com o eps: ')
                try:
                    eps = float(eps)  # VERIFICANDO SE O QUE FOI DIGITADO PARA A 'eps' É UM 'FLOAT'
                    if eps <= 0 or eps >= 1:  # FAZENDO A CONSISTÊNCIA P/ VERIFICAR SE ESTÁ NO INTERVALO INDICADO
                        print('>>>>> ERRO!! Epsylon (eps) fora do intervalo permitido (0, 1).')
                        continue
                    antigovalorEPS = eps  # 'antigovalorEPS' RECEBENDO O VALOR ATUAL DA VARIÁVEL 'eps' P/ SER USADA
                                          # POSTERIORMENTE QUANDO 'cont2 == 1' E NA APRESENTAÇÃO FINAL AO USUÁRIO
                except:
                    if cont == 1:
                        if len(eps) == 0:  # VERIFICANDO SE NÃO FOI DIGITADO NADA PARA A VARIÁVEL 'eps'
                                           # (QUANDO O USUÁRIO DAR 'ENTER' SEM DIGITAR NADA)
                            cont2 = 1  # COMANDO PARA DESIGNAR A VARIÁVEL 'eps' SEU ANTIGO VALOR ('antigovalorEPS')
                            continue
                    print('>>>>> ERRO!! Entrada inválida.')
                else:
                    # SE CHEGAR ATÉ AQUI, ENCERRAR O 'WHILE TRUE' DA VARIÁVEL 'eps'
                    break
        # SE CHEGAR ATÉ AQUI, ENCERRAR O 'WHILE TRUE' DA VARIÁVEL 'entradaX'
        break
    serietaylor = exp(entradaX, eps)  # CÁLCULO A SER FEITO PELA SERIE DE TAYLOR (EXPONENCIAL)
    exponencial = math.exp(entradaX)  # EXPONENCIAL SENDO CÁCULADA PELA FUNÇÃO MATH.EXP
    cont = 1  # VARIÁVEL 'cont' RECEBENDO 1 PARA DIFERENCIAR DA PRIMEIRA VEZ QUE O PROGRAMA RODAR
    # PRINTS PARA MOSTRAR AO USUÁRIO OS CÁLCULOS DA SERIE DE TAYLOR PARA A EXPONENCIAL E PARA A FUNÇÃO MATH.EXP
    print('\nValores calculados para:')
    print('x =', entradaX, '\neps =', eps)
    print('\nExponencial:')
    print('Usando a soma de termos  :    {} '.format(serietaylor))
    print('Usando a função Math.exp :    {} '.format(exponencial))
    print('       |DIFERENÇA|:           {} '.format(math.fabs(exponencial - serietaylor)))
    print('\n* * * * * * * * * * * * * * * * * * * * * * * *')
    print()