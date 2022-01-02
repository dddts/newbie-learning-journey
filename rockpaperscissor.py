import random

winc = 0
losec = 0

def win():
    print("computer:", computerchoice)
    print("playey:", playerchoice)
    print("GGEZ")
    return

def lose():
    print("computer:", computerchoice)
    print("playey:", playerchoice)
    print("你輸了垃圾")
option=["rock" , "paper" , "scissor"]


while True:
    playerchoice=input("rock, paper or scissor?").lower()
    computerchoice=random.choice(option)

    if playerchoice==computerchoice:
        print("computer:",computerchoice)
        print("playey:",playerchoice)
        print("打和啦，Super!")
    elif playerchoice=="rock":
        if computerchoice=="paper":
            lose()
            losec+=1
        if computerchoice=="scissor":
            win()
            winc+=1
    elif playerchoice=="paper":
        if computerchoice=="rock":
            win()
            winc += 1
        if computerchoice=="scissor":
            lose()
            losec += 1
    elif playerchoice=="scissor":
        if computerchoice=="rock":
            lose()
            losec += 1
        if computerchoice=="paper":
            win()
            winc += 1
    elif playerchoice=="":
        continue
    else:
        print("打錯英文啦柒頭")
        continue
    playagain= None
    yn=["y","n"]
    while playagain not in yn:
        playagain=input("play again?(y/n)").lower()
    if playagain=="y":
        print("準備被屌打,你已經打贏{}次,被屌打{}次".format(winc,losec))
    elif playagain=="n":
        print("廢物唔敢玩啦")
        break