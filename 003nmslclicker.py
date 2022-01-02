from tkinter import *
from PIL import ImageTk,Image
def count1():
    global count
    count+=1
    label.config(text=f"你媽死了{count}次")
def reset():
    global count
    count=0
    label.config(text=f"你媽死了{count}次")
def rev():
    global count
    count-=base
    label.config(text=f"你媽死了{count}次")
def autoclick():
    if (x.get() == 1):
        global count
        count+=base
        label.config(text=f"你媽死了{count}次")
        nmsl.after(1000, autoclick)
def lvup():
    global count
    global base
    if count>=100:
        count-=100
        base+=1
base=1
count=0
flag1=False
if count>=100:
    flag1=True
nmsl=Tk()
nmsl.title("nmsl clicker")
x=IntVar()
nmsl.config(background="black")
image=Image.open("nmsl.gif")
nmsl_photo=ImageTk.PhotoImage(image)
button=Button(nmsl,
              command=count1,
              font=("Comic Sans",30),
              bg="black",
              fg="green",
              activebackground="black",
              activeforeground="green",
              image=nmsl_photo,
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
button1.pack(side=BOTTOM)
button2=Button(nmsl,
               text="復活",
               command=rev)
button2.pack(side=BOTTOM)
button3=Checkbutton(nmsl,
                    text="自動死媽1.0",
                    variable=x,
                    onvalue=1,
                    offvalue=0,
                    command=autoclick)
button3.pack(side=BOTTOM)
nmsl.after(1000,autoclick)
button4=Button(nmsl,
               text="升級",
               command=lvup)
if flag1:
    button4.pack(side=BOTTOM)
nmsl.mainloop()
