import time
def entergame():
    while True:
        global name
        name=input("你的名字是?:")
        confirm=None
        yn=["y","n"]

        while confirm not in yn:
            confirm=input("你確定你名字是{}嗎?(y/n)".format(name)).lower()
        if confirm=="y":
            print("哈哈，{}這名字有夠爛".format(name))
            break
        elif confirm=="n":
            print("幹自己的名字都能錯哦")
            continue
standardans=["A","B","C","D"]
count=0

class question:
    def __init__(self,question,ans1,ans2,ans3,ans4,c_ans):
        self.question=question
        self.ans1=ans1
        self.ans2=ans2
        self.ans3=ans3
        self.ans4=ans4
        self.c_ans=c_ans
    def quiz(self):
        global guess
        guess=None
        print("------------------------------------------------")
        print(self.question)
        print(self.ans1)
        print(self.ans2)
        print(self.ans3)
        print(self.ans4)
        while guess not in standardans:
            guess = input("What is your answer?:").upper()
    def check_answer(self):
        global count
        while guess in standardans:
            if guess == self.c_ans:
                count = count + 1
                print("幹你好棒棒哦 你答對了{}題".format(count))
                time.sleep(1.5)
                break
            elif guess != self.c_ans:
                print("幹你老師這麼簡單你都能答錯 有夠爛 再答一次")
                time.sleep(1.5)
                self.quiz()

entergame()
time.sleep(2)
print("等等你將會看到很多有趣的選擇題，請輸入正確的答案")
time.sleep(2)
for seconds in range(5, 0, -1):
    print("遊戲將在{}秒後開始".format(seconds))
    time.sleep(1)
q1=question("q1.誰的媽死了?","A.你媽死了","B.我媽死了","C.他媽死了","D.{}媽死了".format(name),"A")
q2=question("q2.假設大雄有3根棒棒糖，他把2根分給了胖虎，1根自己吃了。請問地球的半徑邊長為多少?","A.大雄其實是被搶吧","B.半徑誰借我量尺量一下","C.我想吃多啦A夢的大棒棒.....糖","D.你媽死了","D")

q1.quiz()
q1.check_answer()
q2.quiz()
q2.check_answer()