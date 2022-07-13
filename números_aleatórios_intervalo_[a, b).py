"""Gera n números aleatórios no intervalo [a, b)"""
from random import randrange
#Gera n números aleatórios no intervalo [a, b)
def GeraAmostra(limite_inf, limite_sup, elementos_amostra):
    amostra = elementos_amostra * [0]
    for k in range(elementos_amostra):
        amostra[k] = limite_inf + float(randrange(1000000)) * (limite_sup - limite_inf)/1000000.0
    return amostra

j = 1
while True:
    if j == 1:
        # COMANDO PARA INICIAR A LEITURA  DO INTERVALO COM OS DADOS INSERIDOS PELO USUÁRIO
        while True:
            print('\n- ENTRE COM O INTERVALO -')
            try:
                limite_inf = float(input('Limite inferior: '))
                limite_sup = float(input('Limite superior: '))
                # VALIDAÇÃO PARA VERIFICAR SE O INTERVALO ESTÁ NAS CONDIÇÕES EXIGIDAS
                if limite_inf >= limite_sup:
                    print('*** ERRO! Limite Inferior do intervalo não pode ser maior ou igual ao Limite Superior.')
                    print('DIGITE AS ENTRADAS NOVAMENTE.')
                    continue
                if limite_sup - limite_inf < 0.001:
                    print('*** ERRO! Tamanho do intervalo tem que ser maior ou igual a 0.001')
                    print('DIGITE AS ENTRADAS NOVAMENTE.')
                    continue
            except:
                print('***ERRO! Entrada inválida! DIGITE A(S) ENTRADA(S) NOVAMENTE.')
                continue
            else:
                while True:
                    # USUÁRIO INSERI A QUANTIDADE DA AMOSTRA
                    try:
                        elementos_amostra = int(input('\nEntre com a quantidade de elementos da amostra: '))
                        # VALIDAÇÃO PARA VERIFICAR SE A QUANTIDADE DA AMOSTRA ESTÁ NAS CONDIÇÕES EXIGIDAS
                        if elementos_amostra <= 0:
                            print('*** ERRO! Entre com um valor inteiro maior que zero')
                            continue
                    except:
                        print('***ERRO! Entrada inválida! DIGITE A(S) ENTRADA(S) NOVAMENTE.')
                        continue
                    else:
                        break
                # CHAMADA DA FUNÇÃO 'GeraAmostra' COM OS PARÂMETROS INSERIDOS PELO USUÁRIO
                amostra = GeraAmostra(limite_inf, limite_sup, elementos_amostra)
                print('\nAmostra: ')
                # EXIBINDO NA TELA A AMOSTRA PSEUDO ALEATÓRIA COM A QUANTIDADE INSERIDA PELO USUÁRIO
                for k in range(elementos_amostra):
                    if k % 10 == 9:
                        print("%10.4f" % amostra[k])
                    else:
                        print("%10.4f" % amostra[k], end=' ')
            # PARA NÃO INICIAR O COMANDO DE LEITURA DE INTERVALO DE NOVO
            j = 0
            break
    # VARIÁVEIS QUE AUXILIARÃO NA CONSTRUÇÃO DOS SUBINTERVALOS
    limitesup_subintervalo = limiteinf_subintervalo = limite_inf
    while True:
        # COMANDO PARA FAZER O USUÁRIO DIGITAR AS ENTRADAS DO INTERVALO E QUANTIDADE DA AMOSTRA DE NOVO
        if j == 1:
            break
        # COMANDO PARA INICIAR A LEITURA DA QUANTIDADE DE SUBINTERVALOS QUE O USUÁRIO DESEJA
        if limitesup_subintervalo == limite_inf:
            try:
                intervalo = int(input('\nEntre com o número de subintervalos do intervalo [{}, {}[ : '.format(limite_inf, limite_sup)))
                # COMANDO PARA VERIFICAR SE A VARIÁVEL 'intervalo' ESTÁ NOS PADRÕES EXIGIDOS
                if intervalo <= 0:
                    print('*** ERRO! Digite um valor maior que zero.')
                    continue
                tamanho_sub_intervalo = (limite_sup - limite_inf) / intervalo
                # COMANDO PARA VERIFICAR SE A VARIÁVEL 'tamanho_sub_intervalo' ESTÁ NO PADRÃO EXIGIDO
                if tamanho_sub_intervalo < 0.001:
                    print('*** ERRO! -- Tamanho do subintervalo é menor que 0.001')
                    print('DIGITE AS ENTRADAS NOVAMENTE.')
                    # j = 1 É PARA FAZER O PR0GRAMA RETORNAR NO SEU INÍCIO
                    j = 1
                    continue
            except:
                print('*** ERRO! Entrada inválida.')
                continue
            else:
                print()
                # MOSTRAR AO USUÁRIO O HISTOGRAMA
                print('\n  Intervalo             Frequência             Gráfico')
        freq = 0
        limitesup_subintervalo = limitesup_subintervalo + tamanho_sub_intervalo
        for i in amostra:
            if limiteinf_subintervalo <= i < limitesup_subintervalo:
                freq += 1
        grafico = freq*"\u2588"
        print("%6.3f" % limiteinf_subintervalo, "A", "%6.3f" % limitesup_subintervalo, "%12.0f" % freq, "                 ", grafico)
        limiteinf_subintervalo = limitesup_subintervalo
        intervalo -= 1
        if intervalo == 0:
            break
