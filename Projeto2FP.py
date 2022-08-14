# Projeto 2 - Fundamentos da Programacao - 1º Semestre

# Pedro Alexandre Chaparro - 99298


# ---------------------------------------------------------------------
#                                TAD posicao
# ---------------------------------------------------------------------

# R. Externa -> 'cl'
# R. Interna -> ('c', 'l')
"""
Representa uma posicao do tabuleiro do jogo do Moinho. Cada posicao e composta
pela coluna (c) e linha (l) que ocupa no tabuleiro (Formato 'cl')
"""

# Construtores
def cria_posicao(c, l):
    # str x str -> posicao
    """
    Recebe duas strings (c = coluna, l = linha) e devolve a posicao
    correspondente.
    """

    if not (c in ('a', 'b', 'c') and l in ('1', '2', '3')):
        raise ValueError('cria_posicao: argumentos invalidos')

    return c, l

def cria_copia_posicao(p):
    # posicao -> posicao
    """
    Recebe uma posicao e devolve uma copia da posicao recebida.
    """
    if not (p[0] in ('a', 'b', 'c') and p[1] in ('1', '2', '3')):
        raise ValueError('cria_copia_posicao: argumentos invalidos')

    return p[0], p[1]



# Seletores
def obter_pos_c(p):
    # posicao -> str
    """
    Recebe uma posicao e devolve a coluna correspondente.
    """
    return p[0]

def obter_pos_l(p):
    # posicao -> str
    """
    Recebe uma posicao e devolve a coluna correspondente.
    """
    return p[1]



# Reconhecedor
def eh_posicao(arg):
    # Universal -> booleano
    """
    Recebe um argumento e devolve True/False, se o argumento for/nao for uma
    posicao.
    """
    return type(arg) == tuple and         \
           len(arg) == 2 and              \
           arg[0] in ('a', 'b', 'c') and  \
           arg[1] in ('1', '2', '3') and  \
           not(type(arg[1]) == bool)



# Teste
def posicoes_iguais(p1, p2):
    # posicao x posicao -> booleano
    """
    Recebe duas posicoes e devolve True/False, se as posicoes forem/nao forem
    iguais.
    """
    return eh_posicao(p1) and eh_posicao(p2) and \
           p1[0] == p2[0] and p1[1] == p2[1]



# Transformador
def posicao_para_str(p):
    # posicao -> str
    """
    Recebe uma posicao e devolve-a no tipo "str" (no formato 'cl')
    """
    return str(p[0]) + str(p[1])



# Funcao de Alto Nivel (FAN)
def obter_posicoes_adjacentes(p):
    # posicao -> Tuplo de Posicoes
    """
    Recebe uma posicao e devolve as posicoes adjacentes, por ordem.
    """
    c = obter_pos_c(p)
    l = obter_pos_l(p)

    if c == 'a' and l == '1':
        return (cria_posicao('b', '1'),
                cria_posicao('a', '2'),
                cria_posicao('b', '2'))

    if c == 'b' and l == '1':
        return (cria_posicao('a', '1'),
                cria_posicao('c', '1'),
                cria_posicao('b', '2'))

    if c == 'c' and l == '1':
        return (cria_posicao('b', '1'),
                cria_posicao('b', '2'),
                cria_posicao('c', '2'))


    if c == 'a' and l == '2':
        return (cria_posicao('a', '1'),
                cria_posicao('b', '2'),
                cria_posicao('a', '3'))

    if c == 'b' and l == '2':
        return (cria_posicao('a', '1'),
                cria_posicao('b', '1'),
                cria_posicao('c', '1'),
                cria_posicao('a', '2'),
                cria_posicao('c', '2'),
                cria_posicao('a', '3'),
                cria_posicao('b', '3'),
                cria_posicao('c', '3'))

    if c == 'c' and l == '2':
        return (cria_posicao('c', '1'),
                cria_posicao('b', '2'),
                cria_posicao('c', '3'))


    if c == 'a' and l == '3':
        return (cria_posicao('a', '2'),
                cria_posicao('b', '2'),
                cria_posicao('b', '3'))

    if c == 'b' and l == '3':
        return (cria_posicao('b', '2'),
                cria_posicao('a', '3'),
                cria_posicao('c', '3'))

    if c == 'c' and l == '3':
        return (cria_posicao('b', '2'),
                cria_posicao('c', '2'),
                cria_posicao('b', '3'))


# --------------------------------------------------------------
#                         TAD peca
# --------------------------------------------------------------

# R. Externa -> [X], [O] ou [ ]
# R. Interna -> 'X', 'O' ou ' ' (igual ao argumento de cria_peca,
#                                                            por convenicencia)
"""
Representa uma peca do tabuleiro do jogo do Moinho. Cada peca e composta pela 
peca que representa o jogador, entre [] que ocupa no tabuleiro (Formato [peca])
"""

# Construtor
def cria_peca(s):
    # str -> peca
    """
    Recebe 'X', 'O' ou ' ', correspondente a um jogador ou a uma peca livre, e
    devolve a peca correspondente.
    """
    if not (s == 'X' or s == 'O' or s == ' '):
        raise ValueError('cria_peca: argumento invalido')

    return s

def cria_copia_peca(j):
    # peca -> peca
    """
    Recebe uma peca e devolve uma copia dela.
    """
    if not (j == 'X' or j == 'O' or j == ' '):
        raise ValueError('cria_copia_peca: argumento invalido')

    return j[0]



# Reconhecedor
def eh_peca(arg):
    # universal -> booleano
    """
    Recebe um argumento e devolve True/False se for/nao for uma peca.
    """
    return arg == 'X' or arg == 'O' or arg == ' '



# Teste
def pecas_iguais(j1, j2):
    # peca x peca -> booleano
    """
    Recebe duas pecas e devolve True/False se as pecas forem/nao forem iguais.
    """
    return eh_peca(j1) and eh_peca(j2) and j1 == j2



# Transformador
def peca_para_str(j):
    # peca -> str
    """
    Recebe uma peca e devolve a representacao externa da mesma.
    """
    if j == 'X':
        return '[X]'
    if j == 'O':
        return '[O]'
    if j == ' ':
        return '[ ]'



# FsAN
def peca_para_inteiro(j):
    # peca -> N
    """
    Recebe uma peca e devolve 1, -1 ou 0 dependendo se a peca recebida e
    'X', 'O' ou ' ', respetivamente.
    """
    if peca_para_str(j) == '[X]':
        return 1
    if peca_para_str(j) == '[O]':
        return -1
    if peca_para_str(j) == '[ ]':
        return 0

def AUX_inteiro_para_peca(i):
    # int -> peca
    """
    Recebe um inteiro 1, -1 ou 0 e devolve a peca que representa.
    """
    if i == 1:
        return cria_peca('X')
    if i == -1:
        return cria_peca('O')
    if i == 0:
        return cria_peca(' ')


# --------------------------------------------------------------
#                         TAD tabuleiro
# --------------------------------------------------------------

# R. Externa ->    a   b   c
#               1 [?]-[?]-[?]
#                  | \ | / |
#               2 [?]-[?]-[?]
#                  | / | \ |
#               3 [?]-[?]-[?]   , onde [?] representa uma [peca]

# R. Interna -> [[!, !, !], [!, !, !], [!, !, !]]
#                               , onde ! representa -1, 0 ou 1 (int)
#                               (lista com 3 listas)
"""
Representa um tabuleiro do jogo do Moinho. Cada tabuleiro e composto pelas 9 
posicoes possiveis, onde em cada uma delas e representada uma peca.
"""

# Todas as posicoes (em string) possiveis, mapeadas com a estrutura de um
# tabuleiro
AUX_posi_string_todas = ('a1', 'b1', 'c1'), \
                        ('a2', 'b2', 'c2'), \
                        ('a3', 'b3', 'c3')

# Todas as linhas e colunas (em string) possiveis
AUX_col_possiveis = ('a', 'b', 'c')
AUX_lin_possiveis = ('1', '2', '3')


# Construtores
def cria_tabuleiro():
    # {} -> tabuleiro
    """
    Devolve um tabuleiro do jogo do moinho vazio (representado por 0).
    """
    vazio = peca_para_inteiro(cria_peca(' '))
    return [[vazio, vazio, vazio],
            [vazio, vazio, vazio],
            [vazio, vazio, vazio]]

def cria_copia_tabuleiro(t):
    # tabuleiro -> tabuleiro
    """
    Recebe um tabuleiro e devolve uma copia dele.
    """
    if not eh_tabuleiro(t):
        raise ValueError('cria_copia_tabuleiro: argumento invalido')

    return [[t[0][0], t[0][1], t[0][2]],
            [t[1][0], t[1][1], t[1][2]],
            [t[2][0], t[2][1], t[2][2]]]



# Seletores
def obter_peca(t, p):
    # tabuleiro x posicao -> peca
    """
    Recebe um tabuleiro e uma posicao e devolve a peca nessa posicao.
    """

    posi_str = posicao_para_str(p)

    for i in range(3):   # Percorre as tres linhas
        # Percorre as posicoes possiveis na linha
        for p_p in AUX_posi_string_todas[i]:
            # Se for a mesma posicao, obtem a linha e coluna
            if p_p == posi_str:
                coluna = i
                linha = AUX_posi_string_todas[i].index(p_p)

    return AUX_inteiro_para_peca(t[coluna][linha])


def obter_vetor(t, s):
    # tabuleiro x str -> tuplo de pecas
    """
    Recebe um tabuleiro e uma string e devolve todas as pecas da linha/coluna
    selecionada pela string.
    """
    # Colunas
    if s == 'a':
        return (AUX_inteiro_para_peca(t[0][0]),
                AUX_inteiro_para_peca(t[1][0]),
                AUX_inteiro_para_peca(t[2][0]))
    elif s == 'b':
        return (AUX_inteiro_para_peca(t[0][1]),
                AUX_inteiro_para_peca(t[1][1]),
                AUX_inteiro_para_peca(t[2][1]))
    elif s == 'c':
        return (AUX_inteiro_para_peca(t[0][2]),
                AUX_inteiro_para_peca(t[1][2]),
                AUX_inteiro_para_peca(t[2][2]))
    # Linhas
    elif s == '1':
        return (AUX_inteiro_para_peca(t[0][0]),
                AUX_inteiro_para_peca(t[0][1]),
                AUX_inteiro_para_peca(t[0][2]))
    elif s == '2':
        return (AUX_inteiro_para_peca(t[1][0]),
                AUX_inteiro_para_peca(t[1][1]),
                AUX_inteiro_para_peca(t[1][2]))
    return (AUX_inteiro_para_peca(t[2][0]),
            AUX_inteiro_para_peca(t[2][1]),
            AUX_inteiro_para_peca(t[2][2]))



# Modificadores
def coloca_peca(t, j, p):
    # tabuleiro x peca x posicao -> tabuleiro
    """
    Recebe um tabuleiro, uma peca e uma posicao; Coloca a peca na posicao
    recebida, retornado o novo tabuleiro (destruindo o antigo).
    """

    linha = int(obter_pos_l(p)) - 1    # String para inteiro - 1
    coluna = ord(obter_pos_c(p)) - 97  # String para inteiro - 'a'

    t[linha][coluna] = peca_para_inteiro(j)

    return t


def remove_peca(t, p):
    # tabuleiro x posicao -> tabuleiro
    """
    Recebe um tabuleiro e uma posicao; Remove a peca da posicao dada e devolve
    o novo tabuleiro (destruindo o antigo).
    """
    linha = int(obter_pos_l(p)) - 1
    coluna = ord(obter_pos_c(p)) - 97

    t[linha][coluna] = peca_para_inteiro(cria_peca(' '))

    return t

def move_peca(t, p1, p2):
    # tabuleiro x posicao x posicao -> tabuleiro
    """
    Recebe um tabuleiro e duas posicoes; Move a peca da primeira posicao dada
    para a segunda posicao e devolve o novo tabuleiro (destruindo o antigo).
    """
    peca = obter_peca(t, p1)
    remove_peca(t, p1)
    coloca_peca(t, peca, p2)

    return t



# Reconhecedores
def eh_tabuleiro(arg):
    # universal -> booleano
    """
    Recebe um argumento e devolve True/False se for/nao for um tabuleiro.
    """
    cont_X = 0       # Contador de [X]
    cont_O = 0       # Contador de [O]
    cont_3linha = 0  # Contador de 3 em linha

    # Argumento e uma lista com tamanho 3
    if type(arg) == list and len(arg) == 3:
        # Todos os 3 argumentos sao listas e tem tamanho 3
        if type(arg[0]) == type(arg[1]) == type(arg[2]) == list and \
           len(arg[0]) == len(arg[1]) == len(arg[2]) == 3:
            # Se tem o formato de um tabuleiro, agora e verificada a validade
            # das pecas. Para isso, percorre as 3 colunas e as 3 linhas
            # possiveis verificado se existem varios 3 em linha e pecas a mais.

            for el in AUX_col_possiveis:
                coluna = obter_vetor(arg, el)
                # Se as 3 pecas da coluna forem iguais...
                if pecas_iguais(coluna[0], coluna[1]) and \
                   pecas_iguais(coluna[0], coluna[2]) and \
                   pecas_iguais(coluna[1], coluna[2]):
                    # e nao forem espacos vazios...
                    if not pecas_iguais(coluna[0], cria_peca(' ')):
                        # entao existe um 3 em linha
                        cont_3linha += 1

                # Verifica o nr de [X] e [O]
                for i in coluna:
                    if pecas_iguais(i, cria_peca('X')):
                        cont_X += 1
                    if pecas_iguais(i, cria_peca('O')):
                        cont_O += 1

            for el in AUX_lin_possiveis:
                linha = obter_vetor(arg, el)

                if pecas_iguais(linha[0], linha[1]) and \
                   pecas_iguais(linha[0], linha[2]) and \
                   pecas_iguais(linha[1], linha[2]):

                    if not pecas_iguais(linha[0], cria_peca(' ')):
                        cont_3linha += 1
                # Nao verifica o nr de [X] e [O] pois estaria a contar duas
                # vezes.

            # Se tudo estiver de acordo com as regras de um tabuleiro, devolve
            # True.
            if cont_3linha <= 1 and cont_X <= 3 and cont_O <= 3:
                if not(cont_X - cont_O > 1 or cont_O - cont_X > 1):

                    return True

    return False

def eh_posicao_livre(t, p):
    # tabuleiro x posicao -> booleano
    """
    Recebe um tabuleiro e uma posicao e devolve True/False se a posicao for ou
    nao for livre.
    """

    for p_l in obter_posicoes_livres(t):
        if posicoes_iguais(p, p_l):
            return True

    return False



# Teste
def tabuleiros_iguais(t1, t2):
    # tabuleiro x tabuleiro -> booleano
    """
    Recebe dois tabuleiros e devolve True/False se forem iguais/diferentes.
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2




# Transformadores
def tabuleiro_para_str(t):
    # tabuleiro -> str
    """
    Recebe um tabuleiro e devolve a sua representao externa.
    """
    # 1a linha do tabuleiro
    a1, b1, c1 = peca_para_str(AUX_inteiro_para_peca(t[0][0])),  \
                     peca_para_str(AUX_inteiro_para_peca(t[0][1])), \
                         peca_para_str(AUX_inteiro_para_peca(t[0][2]))
    # 2a linha
    a2, b2, c2 = peca_para_str(AUX_inteiro_para_peca(t[1][0])), \
                    peca_para_str(AUX_inteiro_para_peca(t[1][1])), \
                        peca_para_str(AUX_inteiro_para_peca(t[1][2]))
    # 3a linha
    a3, b3, c3 = peca_para_str(AUX_inteiro_para_peca(t[2][0])), \
                    peca_para_str(AUX_inteiro_para_peca(t[2][1])), \
                        peca_para_str(AUX_inteiro_para_peca(t[2][2]))

    # linhas da representacao em print() do tabuleiro

    linha1 = '   a   b   c\n'
    linha2 = '1 ' + a1 + '-' + b1 + '-' + c1 + '\n'
    linha3 = '   | \ | / |\n'
    linha4 = '2 ' + a2 + '-' + b2 + '-' + c2 + '\n'
    linha5 = '   | / | \ |\n'
    linha6 = '3 ' + a3 + '-' + b3 + '-' + c3

    return linha1 + linha2 + linha3 + linha4 + linha5 + linha6

def tuplo_para_tabuleiro(t):
    # tuplo -> tabuleiro
    """
    Recebe um tupulo que representa um tabuleiro e devolve o tabuleiro
    """
    t0 = list(t[0])
    t1 = list(t[1])
    t2 = list(t[2])
    return [t0, t1, t2]



# FAL
def obter_ganhador(t):
    # tabuleiro -> peca
    """
    Recebe um tabuleiro, verifica se ha algum ganhador e se sim, devolve a peca
    do vencedor. Caso contrario, devolve uma peca livre.
    """

    # Preparacao para chamar obter_vetor (todos as 3 colunas e 3 linhas)
    vetores_possiveis = AUX_col_possiveis + AUX_lin_possiveis

    for el in vetores_possiveis:
        vetor = obter_vetor(t, el)
        if pecas_iguais(vetor[0], vetor[1]) and \
           pecas_iguais(vetor[0], vetor[2]) and \
           pecas_iguais(vetor[1], vetor[2]) and \
           not pecas_iguais(vetor[0], cria_peca(' ')):
            return vetor[0]

    return cria_peca(' ')


def AUX_tuplo_posicoes_peca(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """
    Recebe um tabuleiro e uma peca e devolve um tuplo com todas as posicoes
    associadas a peca recebida.
    """
    tuplo_posicoes = ()
    for i in range(3):
        for el in AUX_posi_string_todas[i]:

            posi_atual = cria_posicao(el[0], el[1])
            peca_local = obter_peca(t, posi_atual)

            if pecas_iguais(peca_local, j):
                tuplo_posicoes += (posi_atual,)

    return tuplo_posicoes


def obter_posicoes_livres(t):
    # tabuleiro -> tuplo de posicoes
    """
    Recebe um tabuleiro e devolve um tuplo com todas as posiceos livres, por
    ordem.
    """
    return AUX_tuplo_posicoes_peca(t, cria_peca(' '))


def obter_posicoes_jogador(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """
    Recebe um tabuleiro e uma peca e devolve um tupulo com as posicoes ocupadas
    pelo jogador.
    """
    return AUX_tuplo_posicoes_peca(t, j)



# --------------------------------------------------------------
#                   Fase de Colocacao - Regras
# --------------------------------------------------------------

def rule1(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """
    Recebe um tabuleiro e uma peca e devolve, caso exista, um tuplo com a
    posicao onde marcar para ganhar o jogo.
    """

    for posi in obter_posicoes_livres(t):
        vetor_coluna = obter_vetor(t, obter_pos_c(posi))
        vetor_linha = obter_vetor(t, obter_pos_l(posi))
        vetores = vetor_coluna, vetor_linha,
        for vetor in vetores:
            # Se existirem 2 pecas iguais que pertecem ao jogador
            if (pecas_iguais(vetor[0], vetor[1]) and
                pecas_iguais(vetor[1], j)) or \
               (pecas_iguais(vetor[0], vetor[2]) and
                pecas_iguais(vetor[2], j)) or \
               (pecas_iguais(vetor[1], vetor[2]) and
                pecas_iguais(vetor[2], j)):

                return posi,


def rule2(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """
    Recebe um tabuleiro e uma peca e devolve, caso exista, um tuplo com a
    posicao onde marcar para bloquear a vitoria do adversario.
    """
    j_oposto = cria_peca('O')
    if j == cria_peca('O'):
        j_oposto = cria_peca('X')

    return rule1(t, j_oposto)


def rule3(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """
    Recebe um tabuleiro e uma peca e devolve, caso livre, um tuplo com a
    posicao do centro.
    """
    if eh_posicao_livre(t, cria_posicao('b', '2')):
        return cria_posicao('b', '2'),

def rule4(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """
    Recebe um tabuleiro e uma peca e devolve, caso livre, um tuplo com a
    primeira posicao de canto.
    """
    cantos = (cria_posicao('a', '1'),
              cria_posicao('c', '1'),
              cria_posicao('a', '3'),
              cria_posicao('a', '3'))

    for canto in cantos:
        for posi in obter_posicoes_livres(t):
            if posicoes_iguais(posi, canto):
                return posi,

def rule5(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """
    Recebe um tabuleiro e uma peca e devolve, caso livre, um tuplo com a
    primeira posicao de lateral.
    """
    laterais = (cria_posicao('b', '1'),
                cria_posicao('a', '2'),
                cria_posicao('c', '2'),
                cria_posicao('b', '3'))

    for lateral in laterais:
        for posi in obter_posicoes_livres(t):
            if posicoes_iguais(posi, lateral):
                return posi,

# --------------------------------------------------------------
#                          Algoritmo Minimax
# --------------------------------------------------------------

def minimax(t, j, pr, seq_m):
    # tabuleiro x jogador x inteiro x tuplo -> inteiro x tuplo
    """
    Recebe um tabuleiro, um jogador, uma profundidade e uma sequencia de
    movimentose e simula recursivamente todos os tabuleiros possiveis com uma
    jogada (ate uma certa profundidade ou ate existir um vencedor), devolvendo
    o valor do tabuleiro (de quem ganha) e a melhor sequencia de movimentos a
    realizar.
    """

    if pecas_iguais(obter_ganhador(t), cria_peca('X')) or \
       pecas_iguais(obter_ganhador(t), cria_peca('O')) or pr == 0:

        return peca_para_inteiro(obter_ganhador(t)), seq_m
    else:
        o_j = cria_peca('X')
        if j == cria_peca('X'): o_j = cria_peca('O')

        melhor_res = peca_para_inteiro(o_j)
        melhor_seq_m = ()

        for posi_jog in obter_posicoes_jogador(t, j):
            for posi_adj in obter_posicoes_adjacentes(posi_jog):

                if pecas_iguais(obter_peca(t, posi_adj), cria_peca(' ')):

                    novo_tab = cria_copia_tabuleiro(t)
                    novo_movimento = posi_jog, posi_adj
                    move_peca(novo_tab, novo_movimento[0], novo_movimento[1])

                    novo_resultado, nova_seq_m = \
                        minimax(novo_tab, o_j, pr-1, seq_m + novo_movimento)

                    if (melhor_seq_m == ()) or (peca_para_str(j) == '[X]' and
                                               novo_resultado > melhor_res) or\
                        (peca_para_str(j) == '[O]' and novo_resultado <
                                                                   melhor_res):

                        melhor_res, melhor_seq_m = novo_resultado, nova_seq_m

        return melhor_res, melhor_seq_m


# --------------------------------------------------------------
#                         Funcoes Adicionais
# --------------------------------------------------------------

def AUX_Fase_Colocacao(t):
    # tabuleiro -> booleano
    """
    Recebe um tabuleiro e determina a fase atual (fase de colocacao ou de
    movimento), devolvendo True/False se a fase atual for a de colocacao/
    movimento.
    """
    # Se existirem mais de 3 posicoes livres, entao o tabuleiro ainda esta na
    # fase de colocacao
    return len(obter_posicoes_livres(t)) > 3

def AUX_adjacentes_ocupadas(t, p):
    # tabuleiro x posicao -> booleano
    """
    Receve um tabuleiro e uma posicao e devolve True/False se as posicoes
    adjacentes a posicao estiverem todas ocupadas ou nao.
    """
    for posi_livre in obter_posicoes_livres(t):
        for posi_adj in obter_posicoes_adjacentes(p):
            if posicoes_iguais(posi_adj, posi_livre):
                return False

    return True

def AUX_livres_e_adjacentes(t, p1, p2):
    # tabuleiro x posicao x posicao -> booleano
    """
    Recebe um tabuleiro e duas posicoes e devolve True se a segunda posicao
    for uma posicao livre e adjacente a primeira posicao.
    """
    ambas = 0
    for p_l in obter_posicoes_livres(t):
        if ambas <= 1:
            if posicoes_iguais(p_l, p2):
                ambas += 1

    for p_a in obter_posicoes_adjacentes(p1):
        if ambas <= 2:
            if posicoes_iguais(p_a, p2):
                ambas += 1

    return ambas == 2

def obter_movimento_manual(t, j):
    # tabuleiro x peca -> tuplo de posicoes
    """
    Recebe um tabuleiro e uma peca e devolve um tuplo que:
    -contem apenas a posicao escolhida pelo jogador onde colocar uma peca nova,
    na fase de colocacao.
    -contem a posicao de origem da peca que se deja movimentar e a posicao de
    destino.
    """

    if AUX_Fase_Colocacao(t):
        # p_c -> Posicao de Colocacao
        p_c = str(input("Turno do jogador. Escolha uma posicao: "))

        # Se a posicao for uma posicao existente
        if p_c in AUX_posi_string_todas[0] or \
           p_c in AUX_posi_string_todas[1] or \
           p_c in AUX_posi_string_todas[2]:
            # Se for possivel criar a posicao e for uma posicao livre
            p = cria_posicao(p_c[0], p_c[1])

            if eh_posicao(p):
                for p_l in obter_posicoes_livres(t):
                    if posicoes_iguais(p, p_l):

                        return p,

    else:
        posis_movi = str(input("Turno do jogador. Escolha um movimento: "))
        # Se a dimensao da string for 4 (clcl)
        if len(posis_movi) == 4:
            # p1, p2 tomam os valores da string ate verificar se sao posicoes
            p1, p2 = posis_movi[0:2], posis_movi[2:4]

            if (p1 in AUX_posi_string_todas[0] or
                p1 in AUX_posi_string_todas[1] or
                p1 in AUX_posi_string_todas[2]) and \
               (p2 in AUX_posi_string_todas[0] or
                p2 in AUX_posi_string_todas[1] or
                p2 in AUX_posi_string_todas[2]) and \
               pecas_iguais(j, obter_peca(t, cria_posicao(p1[0], p1[1]))):
                #p1, p2 sao agora pecas
                p1, p2 = cria_posicao(p1[0], p1[1]), cria_posicao(p2[0], p2[1])
                # Verificacao logica
                if (AUX_livres_e_adjacentes(t, p1, p2)) or \
                    (posicoes_iguais(p1, p2) and
                     AUX_adjacentes_ocupadas(t, p1)):
                    for p_j in obter_posicoes_jogador(t, j):
                        if posicoes_iguais(p1, p_j):
                            return p1, p2
    # Se nao acontecer nenhum return, entao o input foi incorreto
    raise ValueError('obter_movimento_manual: escolha invalida')

def AUX_lvl_facil(t, j, lvl):
    for p_p_str_lin in AUX_posi_string_todas:
        # Percorre as posicoes em string possiveis (em linha)
        for p_p_str in p_p_str_lin:
            # Para cada posicao possivel em string da linha
            for posi_j in obter_posicoes_jogador(t, j):
                # Para cada posicao do jogador do tabuleiro
                p_p = cria_posicao(p_p_str[0], p_p_str[1])
                # Comparar com a posicao possivel da linha (em strings)
                if posicoes_iguais(p_p, posi_j):
                    # Se coincidirem, percorre as posicoes adjacentes
                    for p_adj in obter_posicoes_adjacentes(posi_j):
                        # Na primeira adjacente livre que encontrar
                        for p_l in obter_posicoes_livres(t):
                            if posicoes_iguais(p_adj, p_l):
                                # Devolve a posicao original e a final
                                return cria_posicao(p_p_str[0],
                                                    p_p_str[1]), p_adj

def AUX_percorre_regras(t, j):
    # tabuleiro x peca -> tuplo de posicao
    """
    Recebe um tabuleiro e uma peca e percorre as regras definidas anteriormente
    devolvendo um tupulo com a posicao mais favoravel.
    """
    # Percorre as regras todas
    if type(rule1(t, j)) == tuple:
        return rule1(t, j)
    if type(rule2(t, j)) == tuple:
        return rule2(t, j)
    if type(rule3(t, j)) == tuple:
        return rule3(t, j)
    if type(rule4(t, j)) == tuple:
        return rule4(t, j)
    return rule5(t, j)

def obter_movimento_auto(t, j, lvl):
    # tabuleiro x peca x str -> tuplo de posicoes
    """
    Recebe um tabuleiro, uma peca e uma string (que representa a dificuldade) e
    devolve  um tuplo com a posicao de colocacao/posicoes de movimento,
    dependendo da fase, que e escolhida automaticamente. A escolha depende do
    nivel de dificuldade escolhido ('facil', 'normal' ou 'dificil').
    Na fase de movimento, se nao for possivel movimentar nenhuma peca, e
    devolvido (posicaoX, posicaoX), ou seja, nao houve movimento.
    """

    if AUX_Fase_Colocacao(t):
        return AUX_percorre_regras(t, j)

    else:
        # Dividido em niveis
        if lvl == 'facil':
            return AUX_lvl_facil(t, j, lvl)

        elif lvl == 'normal':
            seq_movs_mm = minimax(t, j, 1, ())[1]

            return cria_posicao(seq_movs_mm[0][0], seq_movs_mm[0][1]), \
                   cria_posicao(seq_movs_mm[1][0], seq_movs_mm[1][1])

        elif lvl == 'dificil':
            seq_movs_mm = minimax(t, j, 5, ())[1]

            return cria_posicao(seq_movs_mm[0][0], seq_movs_mm[0][1]), \
                   cria_posicao(seq_movs_mm[1][0], seq_movs_mm[1][1])


def moinho(peca_str_j, lvl):
    # str x str -> str
    """
    Recebe a representacao externa de um jogador ('[X]' ou '[O]') e a
    dificuldade ('facil', 'normal' ou 'dificil') e permite jogar um jogo
    completo do jogo do moinho. Devolve o jogador ganhador.
    """
    if not ((peca_str_j == '[X]' or peca_str_j == '[O]') and
            (lvl == 'facil' or lvl == 'normal' or lvl == 'dificil')):
        raise ValueError("moinho: argumentos invalidos")


    j = cria_peca('X')
    j_o = cria_peca('O')

    if peca_str_j == '[O]':
        j = cria_peca('O')
        j_o = cria_peca('X')

    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade " + lvl + ".")

    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))

    #                           FASE DE COLOCACAO

    if peca_str_j == '[X]':  # Se for o jogador a comecar
        coloca_peca(t, j, obter_movimento_manual(t, j)[0])
        print(tabuleiro_para_str(t))

    while AUX_Fase_Colocacao(t):

        # Computador
        if AUX_Fase_Colocacao(t):
            print("Turno do computador (" + lvl + "):")
            coloca_peca(t, j_o, obter_movimento_auto(t, j_o, lvl)[0])
            print(tabuleiro_para_str(t))

            if not pecas_iguais(obter_ganhador(t), cria_peca(' ')):
                return peca_para_str(obter_ganhador(t))

        # Jogador
        if AUX_Fase_Colocacao(t):
            coloca_peca(t, j, obter_movimento_manual(t, j)[0])
            print(tabuleiro_para_str(t))

            if not pecas_iguais(obter_ganhador(t), cria_peca(' ')):
                return peca_para_str(obter_ganhador(t))


    #                       FASE DE MOVIMENTO

    if peca_str_j == '[X]':  # Jogador comeca
        movimento = obter_movimento_manual(t, j)
        move_peca(t, movimento[0], movimento[1])
        print(tabuleiro_para_str(t))

    while not AUX_Fase_Colocacao(t):
        print("Turno do computador (" + lvl + "):")
        move_peca(t, obter_movimento_auto(t, j_o, lvl)[0],
                        obter_movimento_auto(t, j_o, lvl)[1])
        print(tabuleiro_para_str(t))

        if not pecas_iguais(obter_ganhador(t), cria_peca(' ')):
            return peca_para_str(obter_ganhador(t))

        movimento = obter_movimento_manual(t, j)
        move_peca(t, movimento[0], movimento[1])
        print(tabuleiro_para_str(t))

        if not pecas_iguais(obter_ganhador(t), cria_peca(' ')):
            return peca_para_str(obter_ganhador(t))
