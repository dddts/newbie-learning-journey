import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import ImageTk,Image
from pygame import  mixer
def count1():
    global count
    nmsl_sound()
    count+=base
    label.config(text=f"你媽死了{count}次")
    countcheck()
    if count>=100:
        button4.config(state="normal")
def reset():
    global count
    count=0
    countcheck()
    label.config(text=f"你媽死了{count}次")
def rev():
    global count
    count-=base
    countcheck()
    label.config(text=f"你媽死了{count}次")
    if count>=100:
        button4.config(state="normal")
def autoclick():
    if (x.get() == 1):
        global count
        count+=base
        label.config(text=f"你媽死了{count}次")
        countcheck()
        nmsl.after(1000, autoclick)
    if count>=100:
        button4.config(state="normal")
def countcheck():
    if count==742:
        button6.pack(side=BOTTOM)
    else:
        button6.pack_forget()

    global flag1
    global flag2
    if count>=5000:
        button.config(image=nmsl_photo2)
    elif count>=500:
        button.config(image=nmsl_photo1)
    else:
        button.config(image=nmsl_photo0)
    if count>=100:
        if flag1==False and not messagebox.askyesno(title="你媽快死了",message="你還要玩嗎"):
            nmsl.destroy()
        flag1=True
    if count>=1000:
        if flag2==False and not messagebox.askyesno(title="你媽真的快死了",message="你真的還要玩嗎"):
            nmsl.destroy()
        flag2=True

def cheat():
    global count
    global base
    cheatinput=simpledialog.askstring("cheat","please enter your cheat code")
    if cheatinput=="nmsl":
        count+=1000
        label.config(text=f"你媽死了{count}次")
        messagebox.showinfo(title=nmsl,message="你媽多死了1000次")
    if cheatinput=="nnmmssll":
        base+=10
        mixer.music.load(filename="lvup.mp3")
        mixer.music.play()
        messagebox.showinfo(title="nnmmssll",message="levelup!")

def lvup():
    global count
    global base
    global upcount
    global cost
    if count<cost:
        messagebox.showinfo(message="你媽死得不夠徹底")
    if count>=cost:
        count-=cost
        cost = round(cost * 1.05 ** upcount)
        label.config(text=f"你媽死了{count}次")
        button4.config(text=f"升級(${cost})")
        base+=1
        upcount+=1
        countcheck()
def nmsl_sound():
    if count>=5000:
        mixer.music.load(filename="nmslsound2.mp3")
        mixer.music.play()
    elif count>=500:
        mixer.music.load(filename="nmslsound1.mp3")
        mixer.music.play()
    else:
        mixer.music.load(filename="nmslsound.mp3")
        mixer.music.play()
def wally():
    global count
    messagebox.showinfo(title="wow",message="You have found wally")
    mixer.music.load(filename="epicsaxguy.mp3")
    mixer.music.play(loops=-1)
    count+=1000
    label.config(text=f"你媽死了{count}次")

mixer.init()
base=1
count=0
upcount=0
cost=100
flag1=False
flag2=False

#clicker body
nmsl=Tk()
nmsl.title("nmsl clicker")
x=IntVar()
nmsl.config(background="black")
image0=Image.open("nmsl.gif")
nmsl_photo0=ImageTk.PhotoImage(image0)
image1=Image.open("nmsl1.jpg")
nmsl_photo1=ImageTk.PhotoImage(image1)
image2=Image.open("nmsl2.jpg")
nmsl_photo2=ImageTk.PhotoImage(image2)
button=Button(nmsl,
              command=count1,
              font=("Comic Sans",30),
              bg="black",
              fg="green",
              activebackground="black",
              activeforeground="green",
              image=nmsl_photo0,
              compound="bottom",
              padx=80,
              pady=80)
button.pack()
label=Label(nmsl,
            text=f"你媽死了{count}次",
            font=("Comic Sans",30),
            bg="black",
            fg="green",
            )
label.pack(side=TOP)
button1=Button(nmsl,
               text="重設",
               command=reset)
button2=Button(nmsl,
               text="復活",
               command=rev)
button3=Checkbutton(nmsl,
                    text="自動死媽1.0",
                    variable=x,
                    onvalue=1,
                    offvalue=0,
                    command=autoclick)
nmsl.after(1000,autoclick)
button4=Button(nmsl,
               text=f"升級(${cost})",
               command=lvup,
               state="disabled")
button5=Button(nmsl,text="Cheat:)",
               command=cheat,
               bg="black",
               fg="black",
               )
button6=Button(nmsl,text="I'm Wally And You Found Me!",
               command=wally)
button5.pack(anchor="se")
button1.pack(side=BOTTOM)
button2.pack(side=BOTTOM)
button3.pack(side=BOTTOM)
button4.pack(side=BOTTOM)
nmsl.mainloop()
