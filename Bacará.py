#imports
import random as rnd

#Cartas
A = 1
J = 0
Q = 0
K = 0 
fichas = 100
while fichas != 0:
    print(f"Você tem {fichas} fichas")
    #Apostas
    aposta = int(input("Quanto você quer apostar? "))
    if aposta == 0:   #Nao pode apostar 0
        break
    aposta_1 = input("No que voce aposta?(empate,jogador ou banco) ")
    if aposta_1 != "empate" and aposta_1 != "jogador" and aposta_1 != "banco":  #deve apostar em uma das opções
        break
    if aposta != 0:
        #Jogador
        cartaj_1 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, 10]*4)
        cartaj_2 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, 10]*4)
        #Banco
        cartab_1 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, 10]*4)
        cartab_2 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, 10]*4)
        #somas 
        somaj = cartaj_1 + cartaj_2
        somab = cartab_1 + cartab_2
        while jogo:
            if somaj > 10:
                #mudança de tipo do jogador para ajustar a soma (transformar decimais).
                somaj = str(somaj)
                somaj = somaj[-1]
                somaj = int(somaj)
            elif somab > 10:
                #mudança de tipo do banco para ajustar a soma (transformar decimais).
                somab = str(somab)
                somab = somab[-1]
                somab = int(somab)      
            #condicoes de acabar de primeira
            if somaj == 8 or somaj == 9 or somab == 8 or somab == 9:
                if somaj > somab:
                    if aposta_1 == "jogador":  #condição onde o j ganha
                        print("Voce venceu!")
                        fichas += aposta
                        jogo = False
                    if aposta_1 != "banco":    #condição onde o j perde
                        print("Não foi dessa vez!")
                        fichas -= aposta
                        jogo = False
                if somaj == somab:
                    if aposta_1 == "empate":  #condição onde o j ganha
                        print("Voce venceu!")
                        fichas += aposta*8
                        jogo = False
                    if aposta_1 != "empate":  #condição onde o j perde
                        print("Não foi dessa vez!")
                        fichas -= aposta
                        jogo = False
                if somab > somaj:
                    if aposta_1 == "banco":   #condição onde o j ganha
                        print("Voce venceu!")
                        fichas += aposta*0.95
                        jogo = False
                    if aposta_1 != "banco":   #condição onde o j perde
                        print("Não foi dessa vez!")
                        fichas -= aposta
                        jogo = False
            #De comprar cartas
