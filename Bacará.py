#imports
import random as rnd

#Cartas
A = 1
J = 0
Q = 0
K = 0
dez = 0 
fichas = 100
while fichas != 0:
    print(f"Você tem {fichas} fichas")
    #Apostas
    aposta = int(input("Quanto você quer apostar? "))
    if aposta == 0 or aposta > fichas:   #Nao pode apostar 0 nem mais do que tem.
        break
    aposta_1 = input("No que voce aposta?(empate,jogador ou banco) ")
    if aposta_1 != "empate" and aposta_1 != "jogador" and aposta_1 != "banco":  #deve apostar em uma das opções
        break
    if aposta != 0:
        #Jogador
        cartaj_1 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, dez]*4)
        cartaj_2 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, dez]*4)
        #Banco
        cartab_1 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, dez]*4)
        cartab_2 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, dez]*4)
        #somas iniciais
        somab = cartab_1 + cartab_2
        somaj = cartaj_1 + cartaj_2
        #função a ser usada a depois.
        def transforma_decimal(soma):
                    soma = str(soma)
                    soma = soma[-1]
                    soma = int(soma)
                    return soma
        #começa a rodada
        jogo = True
        while jogo: 
            if somaj >= 10:
                #mudança de tipo do jogador para ajustar a soma (transformar decimais).
                somaj = transforma_decimal(somaj) 
            elif somab > 10:
                #mudança de tipo do banco para ajustar a soma (transformar decimais).
                somab = transforma_decimal(somab)      
            #condicoes de acabar de primeira            
            if somaj == 8 or somaj == 9 or somab == 8 or somab == 9:
                #somaj maior que somab
                if somaj > somab:
                    if aposta_1 == "jogador":  #condição onde o j ganha
                        print("Voce venceu!")
                        fichas += aposta
                        jogo = False
                    if aposta_1 != "jogador":
                        print("Não foi dessa vez!")
                        fichas -= aposta
                        jogo = False
                #empate
                if somaj == somab:
                    if aposta_1 == "empate":  #condição onde o j ganha
                        print("Voce venceu!")
                        fichas += aposta*8
                        jogo = False
                    if aposta_1 != "empate":    #condição onde o j perde
                        print("Não foi dessa vez!")
                        fichas -= aposta
                        jogo = False
                #somab maior que somaj
                if somab > somaj:
                    if aposta_1 == "banco":   #condição onde o j ganha
                        print("Voce venceu!")
                        fichas += aposta*0.95
                        jogo = False
                    if aposta_1 != "banco":   #condição onde o j perde
                        print("Não foi dessa vez!")
                        fichas -= aposta
                        jogo = False
            #empate
            if somaj == somab:
                if aposta_1 == "empate":  #condição onde o j ganha
                    print("Voce venceu!")
                    fichas += aposta*8
                    jogo = False
                if aposta_1 != "empate":
                    print("Não foi dessa vez!")
                    fichas -= aposta
                    jogo = False
            #De comprar cartas
               #jogador compra.
            if somaj <= 5:
                carta_3 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, dez]*4)
                somaj += carta_3
                #banco compra.
            if somab <= 5:
                carta_3 = rnd.choice([A, Q, K, J, 2 , 3, 4, 5, 6, 7, 8, 9, dez]*4)
                somab += carta_3
            
