import random
word=['takoyaki',
'pesto',
'enoki',
'dim sum',
'banh beo',
'macaron',
'poutine',
'filet mignon',
'fried rice',
'wonton',
'lo mein',
'chow mein',
'bulgogi',
'kimbap',
'pasta',
'potsticker',
'peking duck',
'croissant',
'eggroll',
'spring roll',
'hummus',
'tator tot',
'naan',
'crepe',
'ahi tuna',
'poke',
'udon',
'sashimi',
'sushi',
'okonomiyaki',
'pad thai',
'fries',
'quesadilla',
'burrito',
'taco',
'jasmine',
'kimchi',
'tofu',
'pizza',
'matcha',
'oolong',
'taro',
'chai',
'tea',
'hu tieu',
'pho',
'bun bo hue',
'bok choy',
'burger',
'dumpling',
'hot pot',
'shabu shabu',
'ramen',
'curry']
while True:
    count=0
    qe=(random.choice(word))
    question=list(qe)
    guess=list("*"*len(question))
    for i, value in enumerate(question):
        if value == " ":
            guess[i] = " "

    while True:
        for j in guess:
            print(j,end="")
        print("\n")
        ans=input("make a guess").lower()
        count+=1
        for i,value in enumerate(question):
            if value==ans:
                guess[i]=ans
        if question==guess:
            print(f"you win, the answer is {qe}")
            if input("wanna start new game?(y/n)").lower=="y":
                break
        if count>9:
            print(f"you r trash, the correct ans is {qe}")
            if input("wanna restart?(y/n)").lower()=="n":
                break

