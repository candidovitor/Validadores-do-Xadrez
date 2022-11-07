import re

tabuleiro =[[0,0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [6,6,6,6,6,6,6,6],
            [1,2,3,4,5,3,2,1]]

tabuleiro_vazio =  [[8,0,0,0,0,0,0,0,0], 
                    [7,0,0,0,0,0,0,0,0],
                    [6,0,0,0,0,0,0,0,0],
                    [5,0,0,0,0,0,0,0,0],
                    [4,0,0,0,0,0,0,0,0],
                    [3,0,0,0,0,0,0,0,0],
                    [2,0,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0,0],
                    ['*','A','B','C','D','E','F','G','H']]

def exibe():
    for l in range(len(tabuleiro)):
        for c in range(len(tabuleiro)):
            if tabuleiro[l][c] == 0:
                print('|_|', end='')
            elif tabuleiro[l][c] == 1:
                print('|T|', end='')
            elif tabuleiro[l][c] == 2:
                print('|C|', end='')
            elif tabuleiro[l][c] == 3:
                print('|B|', end='')
            elif tabuleiro[l][c] == 4:
                print('|D|', end='')
            elif tabuleiro[l][c] == 5:
                print('|R|', end='')
            elif tabuleiro[l][c] == 6:
                print('|P|', end='')
        print('')

def exibe_mapa():
    print('')
    for l in range(len(tabuleiro_vazio)):
        for c in range(len(tabuleiro_vazio)):
            if tabuleiro_vazio[l][c] == 0:
                print('|_|', end='')
            elif tabuleiro_vazio[l][c] == 1:
                print('1 ', end='')
            elif tabuleiro_vazio[l][c] == 2:
                print('2 ', end='')
            elif tabuleiro_vazio[l][c] == 3:
                print('3 ', end='')
            elif tabuleiro_vazio[l][c] == 4:
                print('4 ', end='')
            elif tabuleiro_vazio[l][c] == 5:
                print('5 ', end='')
            elif tabuleiro_vazio[l][c] == 6:
                print('6 ', end='')
            elif tabuleiro_vazio[l][c] == 7:
                print('7 ', end='')
            elif tabuleiro_vazio[l][c] == 8:
                print('8 ', end='')
            elif tabuleiro_vazio[l][c] == '*':
                print('  ', end='')
            elif tabuleiro_vazio[l][c] == 'A':
                print(' A ', end='')
            elif tabuleiro_vazio[l][c] == 'B':
                print(' B ', end='')
            elif tabuleiro_vazio[l][c] == 'C':
                print(' C ', end='')
            elif tabuleiro_vazio[l][c] == 'D':
                print(' D ', end='')
            elif tabuleiro_vazio[l][c] == 'E':
                print(' E ', end='')
            elif tabuleiro_vazio[l][c] == 'F':
                print(' F ', end='')
            elif tabuleiro_vazio[l][c] == 'G':
                print(' G ', end='')
            elif tabuleiro_vazio[l][c] == 'H':
                print(' H ', end='')
            
        print('')
    
def apresentacao():
    print('=-=' * 20)
    print('')
    print('Ola, bem vindo ao validador de jogada do xadrez!')
    print('')
    print('=-=' * 20)
    print('')
    exibe()
    print('')
    print('=-=' * 20)
    print('''Essas são as peças, representadas como: T = Torre: 
                                        C = Cavalo
                                        B = Bispo
                                        D = Dama
                                        R = Rei
                                        P = Peao''')

def jogada1(movimento):
    print('')
    exibe_mapa()
    print('')
    jogada = input('Digite a linha representada e a coluna: ').upper()
            
    while jogada:
        if len(jogada) > 2:
            print('')
            jogada = input('Digite apenas uma letra e um número: ["ex: A4/B7"]').upper()

        elif len(jogada) < 2:
            print('')
            jogada = input('Digite apenas uma letra e um número: ["ex: A4/B7"]').upper()

        elif not re.search("[A-H]",jogada[0]):
            print('')
            jogada = input('Digite apenas uma letra e um número: ["ex: A4/B7"]').upper()

        elif not re.search("[1-8]", jogada[1]):
            print('')
            jogada = input('Digite apenas uma letra e um número: ["ex: A4/B7"]').upper()
        
        else:
            #print(jogada)
            break
    
    for item in jogada:
        movimento.append(item)

    return movimento    

def torres(movimento1, movimento2):
    qnt_casas = True
    has_down = True
    validar_vertical(movimento1, movimento2, qnt_casas, has_down)

def validar_diagonal(movimento1, movimento2):
    coluna = ['A','B','C','D','E','F','G','H']
    linha =  ['1', '2', '3', '4', '5', '6', '7', '8']

    print(f'Seu primeiro movimento foi = {movimento1}')
    print(f'Seu segundo movimento foi = {movimento2}')

    if movimento1[0] == movimento2[0]:
        print('Movimento inválido')
    else:
        if movimento1[1] == movimento2[1]:
            print('Movimento inválido')
        else:
            index_start_coluna = 0
            for i in range(len(coluna)): 
                if movimento1[0] == coluna[i]:
                    index_start_coluna = i

            index_start_linha = 0
            for i in range(len(linha)): 
                if movimento1[1] == linha[i]:
                    index_start_linha = i

            index_end_coluna = 0
            for i in range(len(coluna)): 
                if movimento2[0] == coluna[i]:
                    index_end_coluna = i

            index_end_linha= 0
            for i in range(len(linha)): 
                if movimento2[1] == linha[i]:
                    index_end_linha = i

            """ print(f'index_start_coluna = {index_start_coluna}')
            print(f'index_start_linha = {index_start_linha}')
            print(f'index_end_coluna = {index_end_coluna}')
            print(f'index_end_linha = {index_end_linha}') """

            if abs(index_start_coluna - index_end_coluna) == abs(index_start_linha - index_end_linha):
                #print(f'{index_start_coluna} - {index_end_coluna} == {index_start_linha} - {index_end_linha}')
                print('Movimento valido!')

            else:
                print('Movimento invalido!')

def cavalo(movimento1, movimento2):
    validar_cavalo(movimento1, movimento2)

def validar_cavalo(movimento1, movimento2):
    coluna = ['A','B','C','D','E','F','G','H']
    linha =  ['1', '2', '3', '4', '5', '6', '7', '8']

    if (movimento1[0] == movimento2[0]) or (movimento1[1] == movimento2[1]):
        print('Movimento invalido!')
    else:
        index_start_linha = 0
        index_end_linha = 0
        index_start_coluna = 0
        index_end_coluna = 0

        #movimento1
        for i in range(len(coluna)):
            if movimento1[0] == coluna[i]:
                index_start_linha = i

        #movimento1
        for i in range(len(linha)):
            if movimento1[1] == linha[i]:
                index_end_linha = i

        #movimento2
        for i in range(len(coluna)):
            if movimento2[0] == coluna[i]:
                index_start_coluna = i

        #movimento2
        for i in range(len(linha)):
            if movimento2[1] == linha[i]:
                index_end_coluna = i

        if abs(index_start_linha - index_start_coluna) == 1 or 3:
            if abs(index_end_coluna - index_end_coluna) == 1 or 3:
                print('Movimento valido')
        else:
            print('Movimento invalido!')

def bispo(movimento1, movimento2):
    validar_diagonal(movimento1, movimento2)

def rei(movimento1, movimento2):
    qnt_casas = 1
    has_down = True
    validar_vertical(movimento1, movimento2, qnt_casas, has_down)

def peao(movimento1, movimento2):
    qnt_casas = 1
    has_down = False
    validar_vertical(movimento1, movimento2, qnt_casas, has_down)

def dama(movimento1, movimento2):
    qnt_casas = True
    has_down = True
    if (movimento1[0] == movimento2[0]) or (movimento1[1] == movimento2[1]):
        validar_vertical(movimento1, movimento2, qnt_casas, has_down)
    else:
        validar_diagonal(movimento1, movimento2)

def validar_vertical(movimento1, movimento2, qnt_casas, has_down):
    print(f'Seu primeiro movimento foi = {movimento1}')
    print(f'Seu segundo movimento foi = {movimento2}')
    print('')
    lista_coluna = ['A','B','C','D','E','F','G','H']
    value1 = 0
    value2 = 0

    if has_down == False:
        if type(qnt_casas) == int:
            if (movimento1[0] == movimento2[0]):
                if (movimento2[1] > movimento1[1]):
                    if (int(movimento2[1]) - int(movimento1[1]) == qnt_casas):
                        print('Movimento válido!')
                    else:
                        print('Movimento inválido!')
                else:
                    print('Movimento inválido!')
            else:
                print('Movimento inválido!')
        else:
            print(f' a peça não pode ir para baixo mas pode andar para frente quantas casas quiser')
    else:
        # VALIDANDO MOVIMENTOS PARA TRAS ***** REI *****
        if type(qnt_casas) == int:
            for key, value in enumerate(lista_coluna):
                if value == movimento1[0]:
                    value1 = value1 + (key + 1)

                if value == movimento2[0]:
                    value2 = value2 + (key + 1) 

            if (value2 - value1 > 1) or (value1 - value2 < -1):
                print('Movimento invalido !')
            
            else:
                if (int(movimento1[1]) - int(movimento2[1]) == qnt_casas):
                    print(f'{movimento1[1]} - {movimento2[1]}')
                    print('Movimento valido !  ')

                elif (int(movimento1[1]) - int(movimento2[1]) == -(qnt_casas)):
                    print(f'{movimento1[1]} - {movimento2[1]}')
                    print('Movimento valido ! ')

                elif (int(movimento2[1]) - int(movimento1[1]) == qnt_casas):
                    print(f'{movimento1[1]} - {movimento2[1]}')
                    print('Movimento valido !  ')

                elif (int(movimento2[1]) - int(movimento1[1]) == -(qnt_casas)):
                    print(f'{movimento1[1]} - {movimento2[1]}')
                    print('Movimento valido ! ')
                
                else:
                    print('Movimento invalido! ')

        else:
            #valida torres
            if movimento1[0] == movimento2[0]:
                print('')
                print('Movimento valido!')
                print('')
            elif movimento1[1] == movimento2[1]:
                print('')
                print('Movimento valido!')
                print('')
            else:
                print('')
                print('Movimento invalido!')
                print('')
    
def menu():
    apresentacao()

    pergunta = input('Deseja jogar? [S/N]')

    if pergunta[0] in 'Ss':
        while True:
            variavel = input("Digite a letra da peca: T/C/B/D/R/P ").upper()
            if variavel[0] == 'T':
                print('Voce digitou T de torre!')
                print('')
                movimento1 = jogada1([])
                movimento2 = jogada1([])
                torres(movimento1, movimento2)
            elif variavel[0] == 'C':
                print('Voce digitou C de cavalo!')
                movimento1 = jogada1([])
                movimento2 = jogada1([])
                #validar_diagonal(movimento1, movimento2)
                cavalo(movimento1, movimento2)
            elif variavel[0] == 'B':
                print('Voce digitou B de bispo!')
                movimento1 = jogada1([])
                movimento2 = jogada1([])
                #validar_diagonal(movimento1, movimento2)
                bispo(movimento1, movimento2)
            elif variavel[0] == 'D':
                print('Voce digitou D de dama!')
                movimento1 = jogada1([])
                movimento2 = jogada1([])
                dama(movimento1, movimento2)
            elif variavel[0] == 'R':
                print('Voce digitou R de rei!')
                print('')
                movimento1 = jogada1([])
                movimento2 = jogada1([])
                rei(movimento1, movimento2)
            elif variavel[0] == 'P':
                print('Voce digitou P de peão!')
                print('')
                movimento1 = jogada1([])
                movimento2 = jogada1([])
                #validar_vertical(movimento1, movimento2, qnt_casas, has_down)
                peao(movimento1, movimento2)

            elif not re.search("[T,C,B,D,R,P]",variavel[0]):
                print('Não entendi o que você quis dizer!')

    else:
        print(f'Voce digitou {pergunta} Logo entendi que você nao quer jogar! Até outra hora!')

menu()