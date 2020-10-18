# EP - Design de Software
# Equipe: Ricardo Ribeiro Rodrigues
# Data: 09/10/2020
#imports
import random as rnd
#Cartas
A = 1
J = 0
Q = 0
K = 0
dez = 0
#Baralhos usados.
baralhos = [A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, dez]*4*8   #8 baralhos  
#jogadores
n = int(input("Quantos jogadores serão?? "))
#fichas iniciais
fichas = [1000]*n
#teste para a rodada
jogo = True 
#funções a serem usadas depois.
def transforma_decimal(soma):
    if soma >= 10:
        soma = str(soma)
        soma = soma[-1]
        soma = int(soma)
        return soma
    else:
        return soma
def fim_do_jogo(somaj,somab,fichas,jogo):
    if somaj == 8 or somaj == 9 or somab == 8 or somab == 9 or t == 1:
        i = 0 #contador a ser usado
        #somaj maior que somab
        if somaj > somab:
            while i < n:
                if lista_apostas_ejb[i] == "jogador":  #condição onde o j ganha
                    print('\033[32m' + f"Voce venceu jogador {i+1}!" + '\033[0;0m')
                    fichas[i] += lista_apostas_num[i] - lista_apostas_num[i]*0.0124   #1.24% de comissao
                    jogo = False #acaba a rodada
                if lista_apostas_ejb[i] != "jogador":
                    print('\033[31m' + f"Não foi dessa vez jogador {i+1}" + '\033[0;0m')
                    fichas[i] -= lista_apostas_num[i]
                    jogo = False #acaba a rodada
                i += 1
            return fichas, jogo
        #empate
        if somaj == somab:
            while i < n:
                if lista_apostas_ejb[i] == "empate":  #condição onde o j ganha
                    print('\033[32m' + f"Voce venceu jogador {i+1}!" + '\033[0;0m')
                    fichas[i] += lista_apostas_num[i]*8 - lista_apostas_num[i]*0.1436   #14.36% de comissao  
                    jogo = False #acaba a rodada
                if lista_apostas_ejb[i] != "empate":    #condição onde o j perde
                    print('\033[31m' + f"Não foi dessa vez jogador {i+1}" + '\033[0;0m')
                    fichas[i] -= lista_apostas_num[i] 
                    jogo = False #acaba a rodada
                i += 1
            return fichas, jogo
        #somab maior que somaj
        if somab > somaj:
            while i < n:
                if lista_apostas_ejb[i] == "banco":   #condição onde o j ganha
                    print('\033[32m' + f"Voce venceu jogador {i+1}!" + '\033[0;0m')
                    fichas[i] += lista_apostas_num[i]*0.95 - lista_apostas_num[i]*0.0106  #1.06% de comissao
                    jogo = False #acaba a rodada
                if lista_apostas_ejb[i] != "banco":   #condição onde o j perde
                    print('\033[31m' + f"Não foi dessa vez jogador {i+1}" + '\033[0;0m')
                    fichas[i] -= lista_apostas_num[i]
                    jogo = False #acaba a rodada
                i += 1
            return fichas, jogo
    else:
        return fichas, jogo
#regras avancadas para o banco comprar.
def terceira_carta_b(somaj,somab):
    if ((somaj <= 5) == False):  #se o jogador nao recebeu
        if somab <= 5:  #se a soma é menor ou igual a 5
            carta_3b = rnd.choice(baralhos)
            print('\033[33m' + f"O banco recebe a 3° carta com valor de: {carta_3b}" + '\033[0;0m')
            return carta_3b
        else:   #se não é (para nao dar none)
            return 0 
    if (somaj <= 5) == True and somab <= 5:   #se o jogador recebeu
        if carta_3j == 8 and somab == 3:  
            #nao recebe
            return 0                   
        if somab == 4 and (carta_3j == 0 or carta_3j == 1 or carta_3j == 8 or carta_3j == 9):
            #nao recebe
            return 0
        if somab == 5 and (carta_3j == 0 or carta_3j == 1 or carta_3j == 2 or carta_3j == 3 or carta_3j == 8 or carta_3j == 9):
            #nao recebe
            return 0
        else:  #recebe
            carta_3b = rnd.choice(baralhos)
            print('\033[33m' + f"O banco recebe a 3° carta com valor de: {carta_3b}" + '\033[0;0m')
            return carta_3b
    else:
        return 0 
#Jogo em si
while 0 not in fichas:  #Se acabar as fichas de algum dos players, acaba o jogo.
    i = 0
    #print das fichas de todos os players.
    while i < n:
        print('\033[34m' + f"O jogador {i+1} tem {fichas[i]:.0f} fichas" + '\033[0;0m')  #fichas inteiras apenas.
        i += 1
    #Apostas
    i = 0
    lista_apostas_num = [] #listas onde estarão as apostas numéricas de cada um dos jogadores.
    lista_apostas_ejb = [] #lista onde estarão em quem cada um dos jogadores apostou.
    while i < n:
        aposta = int(input('\033[35m' + f"Quanto o jogador {i+1} vai apostar? " + '\033[0;0m'))
        if aposta == 0 or aposta > fichas[i]:   #Nao pode apostar 0 nem mais do que tem.
            break
        lista_apostas_num.append(aposta) 
        i += 1
    i = 0
    while i < n:
        aposta_1 = input('\033[35m' + f"No que o jogador {i+1} aposta?(empate,jogador ou banco) " + '\033[0;0m')
        if aposta_1 != "empate" and aposta_1 != "jogador" and aposta_1 != "banco":  #deve apostar em uma das opções
            break
        lista_apostas_ejb.append(aposta_1)
        i += 1
    #Cartas do jogador
    cartaj_1 = rnd.choice(baralhos)
    cartaj_2 = rnd.choice(baralhos)
    #Cartas do banco
    cartab_1 = rnd.choice(baralhos)
    cartab_2 = rnd.choice(baralhos)
    #somas iniciais
    somab = cartab_1 + cartab_2
    somaj = cartaj_1 + cartaj_2
    #começa a rodada
    t = 0
    jogo = True
    #Muda a soma do jogador para apenas o ultimo numero.
    somaj = transforma_decimal(somaj) 
    #Muda a soma do banco para apenas o ultimo numero.
    somab = transforma_decimal(somab)
    #print das somas      
    print(f"a soma do jogador vale {somaj}")
    print(f"a soma do banco vale {somab}")
    #condicoes de acabar de primeira
    resultado_tuple = fim_do_jogo(somaj,somab,fichas,jogo)
    fichas = resultado_tuple[0]
    jogo = resultado_tuple[1]
    #Se nao tiver acabado
    if jogo:
        #De comprar cartas
        #jogador comprar.
        if somaj <= 5:
            carta_3j = rnd.choice(baralhos)
            print('\033[33m' + f"O jogador recebe a 3° carta com valor de: {carta_3j}" + '\033[0;0m')
            somaj += carta_3j
        #se o valor for igual a 0, ele comprou uma carta de valor 0 ou nao comprou (Nao afeta a soma)
        somab += terceira_carta_b(somaj,somab)
        #transformação dos decimais
        #jogador
        somaj = transforma_decimal(somaj)
        #banco
        somab = transforma_decimal(somab)
        #para fechar o jogo
        t = 1
        resultado_tuple = fim_do_jogo(somaj,somab,fichas,jogo)
        fichas = resultado_tuple[0]
        jogo = resultado_tuple[1]