import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
def count1():
    global count
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
    if count>=500:
        button.config(image=nmsl_photo2)
    elif count>=100:
        button.config(image=nmsl_photo1)
    else:
        button.config(image=nmsl_photo0)
def lvup():
    global count
    global base
    global upcount
    if count>=cost:
        count-=cost
        label.config(text=f"你媽死了{count}次")
        button4.config(text=f"升級(${cost})")
        base+=1
        upcount+=1
        countcheck()
        print(upcount)
        print(cost)
base=111
count=0
upcount=0
cost=(100*1.87**upcount)


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
               text=f"升級(${cost})",
               command=lvup,
               state="disabled")


button4.pack(side=BOTTOM)
nmsl.mainloop()
