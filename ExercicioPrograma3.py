from random import randrange
def LeiaMatriz(NomeArq):
    # Lê e retorna uma matriz contendo todas as apostas da megasena.
    # Cada linha contém:
    # mat[][0] - int - número do sorteio
    # mat[][1] - str - data do sorteio
    # mat[][2..7] - int - cada número sorteado (1 a 60)
    # Retorna None se houve algum erro na leitura.
    mat = [] # inicia a matriz

    # abrir o arquivo para leitura
    try:
        arq = open(NomeArq, "r")
    except:
        print("\nErro na abertura do arquivo (open)")
        return None
    # ler cada uma das linhas do arquivo
    i = 0
    for linha in arq:
        # se der alguma exception retorna None
        try:
            lin = linha[:len(linha) - 1] # tira o \n do final
            v = lin.split('\t')# separa os elementos da string
            mat.append([]) # adiciona uma nova linha a matriz
            # Transforma os strings numéricos em números inteiros
            for j in range(8):
                if j == 1:
                    mat[i].append(v[1])
                else:
                    mat[i].append(int(v[j]))
            i = i + 1
        except:
             # algum erro no trecho acima
             print("Erro no split(), no int() ou no append()")
             return None
    arq.close()
    return mat

def EscolheAposta(nt):
    NumerosSorteados = nt*[0]
    i = 0
    while True:
        # Sorteia um número e atribui à uma posição da lista
        NumerosSorteados[i] = randrange(1, 61)
        if i >= 1:
            # Verificar se tem número repetido na lista do sorteio
            if NumerosSorteados[i] in NumerosSorteados[:i]:
                i -= 1
        i += 1
        if i == nt:
            break
    return NumerosSorteados
# Para iniciar a leitura do arquivo
i = 0
print('Leitura do arquivo de sorteios')
print('Montagem da tabela de último sorteio de cada número')
print()
while True:
    if i == 0:
        # Leitura do arquivo
        narq = input("Entre com o nome do arquivo: ")
        # Chamando a função
        arquivo = LeiaMatriz(narq)
        # Verifica se o programa conseguiu ler o arquivo
        if arquivo == None:
            print('\nDigite novamente o nome do arquivo.')
            continue
        else:
            # Para não voltar a ler o arquivo de novo
            i = 1
    try:
        qnumaposta = int(input('\nQuantidade de números da aposta: '))
        if qnumaposta < 6 or qnumaposta > 12:
            print('>>> ERRO! Digite uma quantidade inteira entre 6 e 12')
            continue
    except:
        print('\n>>> ERRO! Entrada Inválida!')
        print('Digite uma quantidade inteira entre 6 e 12')
        continue
    else:
        # Chamando a função para gerar uma aposta pseudo aleatória
        aposta = EscolheAposta(qnumaposta)
        print('Aposta escolhida - {} números:'.format(qnumaposta))
        # Mostrando ao usuário a aposta gerada
        for i in aposta:
            print(i, end="  ")
        print()
        # Verificando se a aposta gerada é uma aposta válida (nunca foi sorteada)
        for i in range(len(arquivo)):
            j = 0
            # Contador
            cont = 0
            # variável auxiliar para brecar o while
            AuxNumAposta = qnumaposta
            while True:
                if aposta[j] not in arquivo[i][2:8]:
                    AuxNumAposta -= 1
                else:
                    # Se o número estiver dentro de uma aposta vencedora, somar mais um ao contador
                    cont += 1
                # Sair do while quando no máximo 5 números da sua aposta podem pertencer à uma aposta vencedora
                if AuxNumAposta == 5:
                    break
                j += 1
                if cont == 6:
                    numsorteio = arquivo[i][0]
                    datasorteio = arquivo[i][1]
                    break
            if cont == 6:
                # Pular fora do 'for' e i = 1 é para não acionar o comando de leitura do arquivo de novo, caso i == 0
                i = 1
                break
        # Mostrando ao usuário se sua aposta é válida ou não
        if AuxNumAposta < 6:
            print('*** Aposta válida')
        else:
            print('*** Aposta inválida')
            print('*** Números já sorteados no sorteio {} de {}'.format(numsorteio, datasorteio))