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
#fichas iniciais
fichas = 100
#testa para a rodada
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
        #somaj maior que somab
        if somaj > somab:
            if aposta_1 == "jogador":  #condição onde o j ganha
                print('\033[32m' + "Voce venceu!" + '\033[0;0m')
                fichas += aposta - aposta*0.0124   #1.24% de comissao
                jogo = False
                return fichas, jogo
            if aposta_1 != "jogador":
                print('\033[31m' + "Não foi dessa vez!" + '\033[0;0m')
                fichas -= aposta
                jogo = False
                return fichas, jogo
        #empate
        if somaj == somab:
            if aposta_1 == "empate":  #condição onde o j ganha
                print('\033[32m' + "Voce venceu!" + '\033[0;0m')
                fichas += aposta*8 - aposta*0.1436   #14.36% de comissao  
                jogo = False
                return fichas, jogo
            if aposta_1 != "empate":    #condição onde o j perde
                print('\033[31m' + "Não foi dessa vez!" + '\033[0;0m')
                fichas -= aposta
                jogo = False
                return fichas, jogo
        #somab maior que somaj
        if somab > somaj:
            if aposta_1 == "banco":   #condição onde o j ganha
                print('\033[32m' + "Voce venceu!" + '\033[0;0m')
                fichas += aposta*0.95 - aposta*0.0106  #1.06% de comissao
                jogo = False
                return fichas, jogo
            if aposta_1 != "banco":   #condição onde o j perde
                print('\033[31m' + "Não foi dessa vez!" + '\033[0;0m')
                fichas -= aposta
                jogo = False
                return fichas, jogo
    else:
        return fichas, jogo
#regras avancadas para o banco comprar.
def terceira_carta_b(somaj,somab):
    if ((somaj <= 5) == False):  #se o jogador nao recebeu
        if somab <= 5:  #se a soma é menor ou igual a 5
            carta_3b = rnd.choice(baralhos)
            print('\033[33m' + f"banco recebe a carta: {carta_3b}" + '\033[0;0m')
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
            print('\033[33m' + f"banco recebe a carta: {carta_3b}" + '\033[0;0m')
            return carta_3b
    else:
        return 0 
#Jogo em si
while fichas != 0:
    print('\033[34m' + f"Você tem {fichas} fichas" + '\033[0;0m')
    #Apostas
    aposta = int(input("Quanto você quer apostar? "))
    if aposta == 0 or aposta > fichas:   #Nao pode apostar 0 nem mais do que tem.
        break
    aposta_1 = input("No que voce aposta?(empate,jogador ou banco) ")
    if aposta_1 != "empate" and aposta_1 != "jogador" and aposta_1 != "banco":  #deve apostar em uma das opções
        break

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
    #mudança de tipo do jogador para ajustar a soma (transformar decimais).
    somaj = transforma_decimal(somaj) 
    #mudança de tipo do banco para ajustar a soma (transformar decimais).
    somab = transforma_decimal(somab)      
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
            print('\033[33m' + f"jogador recebe a carta: {carta_3j}" + '\033[0;0m')
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


