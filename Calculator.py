#importing tkinter module
from tkinter import*
root=Tk()
root.geometry("300x450")
#Creating the entry box
e=Entry(root, width=40, borderwidth=3)
e.pack()
#Naming our application
root.title("Calculator")
#Setting background colour
root.config(bg="light yellow")
#Backend for click
def click(n):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(n))
#Backend for calculation
def add():
    n1=e.get()
    global i
    i=int(n1)
    global math
    math="add"
    e.delete(0,END)
def sub():
    n1=e.get()
    global i
    i=int(n1)
    global math
    math="sub"
    e.delete(0, END)
def mul():
    n1=e.get()
    global i
    i=int(n1)
    global math
    math="mul"
    e.delete(0, END)
def div():
    n1=e.get()
    global i
    i=int(n1)
    global math
    math="div"
    e.delete(0, END)
def calculate():
    n2=e.get()
    e.delete(0,END)

    if math=="add":
        e.insert(0,i + int(n2))
    elif math=="sub":
        e.insert(0,i - int(n2))
    elif math=="mul":
        e.insert(0,i * int(n2))
    elif math=="div":
        e.insert(0,i / int(n2))
def clear():
    e.delete(0,END)
def close():
    root.destroy()
#Creating the buttons
b1=Button(root,text=1,height=2,width=4,command=lambda:click(1),bg="blue",fg="white",font=("bold"))
b1.place(x=50,y=60)

b2=Button(root,text=2,height=2,width=4,command=lambda:click(2),bg="blue",fg="white",font=("bold"))
b2.place(x=130,y=60)

b3=Button(root,text=3,height=2,width=4,command=lambda:click(3),bg="blue",fg="white",font=("bold"))
b3.place(x=210,y=60)

b4=Button(root,text=4,height=2,width=4,command=lambda:click(4),bg="blue",fg="white",font=("bold"))
b4.place(x=50,y=120)

b5=Button(root,text=5,height=2,width=4,command=lambda:click(5),bg="blue",fg="white",font=("bold"))
b5.place(x=130,y=120)

b6=Button(root,text=6,height=2,width=4,command=lambda:click(6),bg="blue",fg="white",font=("bold"))
b6.place(x=210,y=120)

b7=Button(root,text=7,height=2,width=4,command=lambda:click(7),bg="blue",fg="white",font=("bold"))
b7.place(x=50,y=180)

b8=Button(root,text=8,height=2,width=4,command=lambda:click(8),bg="blue",fg="white",font=("bold"))
b8.place(x=130,y=180)

b9=Button(root,text=9,height=2,width=4,command=lambda:click(9),bg="blue",fg="white",font=("bold"))
b9.place(x=210,y=180)

b0=Button(root,text=0,height=2,width=4,command=lambda:click(0),bg="blue",fg="white",font=("bold"))
b0.place(x=50,y=240)

badd=Button(root,text="+",height=2,width=4,command=add,bg="blue",fg="white",font=("bold"))
badd.place(x=130,y=240)

bsub=Button(root,text="-",height=2,width=4,command=sub,bg="blue",fg="white",font=("bold"))
bsub.place(x=210,y=240)

bm=Button(root,text="X",height=2,width=4,command=mul,bg="blue",fg="white",font=("bold"))
bm.place(x=50,y=300)

bd=Button(root,text="/",height=2,width=4,command=div,bg="blue",fg="white",font=("bold"))
bd.place(x=130,y=300)

beq=Button(root,text="=",height=2,width=4,command=calculate,bg="blue",fg="white",font=("bold"))
beq.place(x=210,y=300)

bclr=Button(root,text="clear",height=2,width=4,command=clear,bg="blue",fg="white",font=("bold"))
bclr.place(x=50,y=360)

bcls=Button(root,text="close",height=2,width=4,command=close,bg="blue",fg="white",font=("bold"))
bcls.place(x=130,y=360)

mainloop()
