#imports
import random as rnd

#Cartas
A = 1
J = 0
Q = 0
K = 0 
fichas = 100
while fichas != 0:
    #Apostas
    aposta = int(input("Quanto você quer apostar? "))
    aposta_1 = input("No que voce aposta?(empate,jogador ou banco) ")
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
        #condicoes de acabar de primeira
        if somaj == 8 or 9 or somab == 8 or 9:
            if somaj > somab:
                if aposta_1 == "jogador":
                    print("Voce venceu!")
                    fichas += aposta
            if somaj == somab:
                if aposta_1 == "empate":
                    print("Voce venceu!")
                    fichas += aposta*8
            if somab > somaj:
                if aposta_1 == "banco":
                    print("Voce venceu!")
                    fichas += aposta*0.95
        #De comprar cartas
