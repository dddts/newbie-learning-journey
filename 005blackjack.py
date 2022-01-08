import random
while True:
    cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    colors=["s","c","h","d"]
    deck=[]
    playerhand=[]
    computerhand=[]
    for color in colors:
        for card in cards:
            deck.append((card,color))
    def sumcheck():
        global playersum
        playersum = 0
        for value,co in playerhand:
            if value=="2":
                playersum+=2
            elif value=="3":
                playersum+=3
            elif value=="4":
                playersum+=4
            elif value=="5":
                playersum+=5
            elif value=="6":
                playersum+=6
            elif value=="7":
                playersum+=7
            elif value=="8":
                playersum+=8
            elif value=="9":
                playersum+=9
            elif value=="10":
                playersum+=10
            elif value=="J":
                playersum+=10
            elif value=="Q":
                playersum+=10
            elif value=="K":
                playersum+=10
        for value, face in playerhand:
            if value == "A":
                if playersum >= 11:
                    playersum += 1
                elif playersum < 11:
                    playersum += 11
    def computersumcheck():
        global computersum
        computersum = 0
        for value,co in computerhand:
            if value=="2":
                computersum+=2
            elif value=="3":
                computersum+=3
            elif value=="4":
                computersum+=4
            elif value=="5":
                computersum+=5
            elif value=="6":
                computersum+=6
            elif value=="7":
                computersum+=7
            elif value=="8":
                computersum+=8
            elif value=="9":
                computersum+=9
            elif value=="10":
                computersum+=10
            elif value=="J":
                computersum+=10
            elif value=="Q":
                computersum+=10
            elif value=="K":
                computersum+=10
        for value, face in computerhand:
            if value=="A":
                if computersum>=11:
                    computersum+=1
                elif computersum<11:
                    computersum+=11
        while computersum<17:
            computerhand.append(deck.pop())
            computersumcheck()
    def shuffle():
        random.shuffle(deck)
    def start():
        global decision
        playerhand.append(deck.pop())
        playerhand.append(deck.pop())
        computerhand.append(deck.pop())
        sumcheck()
        print(f"your hand is {playerhand}")
        print(f'computer hand is {computerhand}+?')
    def hitorstand():
        while True:
            decision=None
            hs=['hit','stand']
            while decision not in hs:
                decision=input("hit or stand").lower()
            if decision=="hit":
                playerhand.append(deck.pop())
                sumcheck()
                print(f'your hand is {playerhand}')
                print(f"computerhand is : {computerhand}")
                if playersum > 21:
                    print('you lose100')
                    print(playersum)
                    break
            if decision=="stand":
                computersumcheck()
                print(f"playerhand is : {playerhand}")
                print(f"computerhand is : {computerhand}")
                if computersum>21:
                    print('you win107')
                    break
                elif computersum==playersum:
                    print("draw109")
                    break
                elif computersum>playersum:
                    print("you lose111")
                    break
                elif playersum>computersum:
                    print("you win113")
                    break

    shuffle()
    start()
    if playersum==21:
        print("wow blackjack, you win")
    else:
        hitorstand()
    yn=['y','n']
    rgame=None
    while rgame not in yn:
        rgame=input("do you want to restart game?(y/n)").lower()
    if rgame=="y":
        continue
    if rgame=="n":
        break
