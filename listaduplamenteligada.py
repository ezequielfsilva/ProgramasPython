# Nome: Ezequiel Ferreira da Silva
# NUSP: 10092486
# Exercícios 3

class ListaDuplamenteLigada:
    ''' operações sobre uma lista duplamente ligada. '''
    # classe _Node - interna
    class _Node:
        __slots__ = '_info', '_prev', '_prox'

        def __init__ (self, info, prev, prox):
             # inicia os campos
             self._info = info
             self._prev = prev
             self._prox = prox

    # métodos de lista duplamente ligada
    def __init__ (self):
        ''' cria uma lista circular vazia.'''
        self._inicio = self._Node(None, None, None) # vazia
        self._final = self._Node(None, None, None) # vazia
        self._inicio._prox = self._final
        self._final._prev = self._inicio
        self._tamanho = 0 # tamanho da lista

    def __len__(self):
        ''' retorna o tamanho da LL.'''
        return self._tamanho

    def is_empty(self):
        ''' retorna True se LL vazia'''
        return self._tamanho == 0

    def first(self):
        ''' retorna o campo info da LL sem remover.
        sinaliza exceção se LL vazia.'''
        if self.is_empty():
            raise Empty("Lista Ligada Vazia")
        return self._inicio._info  # elemento inicial da fila

    def adiciona(self, e):
        ''' adiciona elemento no inicio da LL.'''
        # novo nó referencia o inicio da LL
        novo = self._Node(e, self._inicio)
        # novo nó será o inicio da LL
        self._inicio = novo
        self._tamanho += 1

    def adiciona_afrente(self, p, e):
        ''' adiciona elemento a frente de p.'''
        # novo nó referencia o mesmo que p
        novo = self._Node(e, p._prox)
        # p referencia o novo nó
        p._prox = novo
        self._tamanho += 1

    def remove_afrente(self, p):
        ''' remove elemento a frente de p.'''
        # caso particular - p não pode ser o último
        if p._prox is None:
            raise Empty("Nó inexistente")
        # p referencia o mesmo que o próximo
        p._prox = p._prox._prox
        self._tamanho -= 1

    def busca(self, e):
        ''' procura elemento com info = e.
        devolve referência para esse elemento ou None.'''
        # p percorre a lista
        p = self._inicio
        while p is not None:
            if p._info == e: return p  # achou
        p = p._prox  # vai para o próximo
        # se chegou aqui é porque não achou
        return None

    def busca_ant(self, e):
        ''' procura elemento com info = e.
        devolve uma dupla de referências (p_ant, p).'''

        # p percorre a lista e pant referencia o anterior
        pant, p = None, self._inicio
        while p is not None:
            if p._info == e:
                return pant, p
            pant, p = p, p._prox
        return pant, p


    def CriaLL(self, vet):
        ''' cria uma LL com elementos do vetor vet.'''
        for k in range(len(vet) - 1, -1, -1):
            self.adiciona(vet[k])


    def ImprimeLL(self):
        ''' só para teste.'''
        p = self._inicio
        k = 1
        print("Imprimindo a lista ligada:")
        while p is not None:
            print(k, " - ", p._info)
            k = k + 1
            p = p._prox

    def adicionar_entre(self, e, anterior, sucessor):
        ''' adiciona elemento entre 2 outros.
        retorna o novo nó.'''
        novo = self._Node(e, anterior, sucessor)
        anterior._prox = novo
        sucessor._prev = novo
        self._tamanho += 1
        return novo

    def remove(self, node):
        ''' remove nó da lista e retorna seu valor.'''
        anterior = node._prev
        sucessor = node._prox
        anterior._prox = sucessor
        sucessor._prev = anterior
        self._tamanho -= 1
        val = node._info  # guarda a informação
        # inative o nó
        node._prev = node._prox = node._info = None
        return val
'''
def Conta (LA, x):
# devolve quantos nós da lista duplamente ligada LA com info == x.

def Adiciona(LA, x):
# Adiciona novo elemento com info == x na lista duplamente ligada LA.
# Mantém a ordem crescente.

def Remove(LA, x):
# Remove todos os elementos com info == x da lista duplamente ligada LA.
# Estarão contíguos.

def __str__(LA):
# Mostra os elementos da lista duplamente ligada.
# Mostra também o anterior e o sucessor.
'''

lx = ListaDuplamenteLigada()
while True:
    f = input("Entre com a informação:")
    if f == 'fim': break
    lx.adicionar_entre(f)
    print(lx)
# teste remover
'''
while True:
    f = input("Entre com a informação a remover:")
    if f == 'fim': break
    print("removidos", lx.Remove(f), "elementos")
    print(lx)
# teste conta
while True:
    f = input("Entre com a informação a contar:")
    if f == 'fim': break
    print("contados", lx.Conta(f), "elementos")
    print(lx)
'''