from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Money Counter App")
root.configure(bg="light green")
root.geometry("400x400")
l1=Label(root,text="Welcome to Money Counter App")
l1.place(relx=0.5,rely=0.5,anchor=CENTER)

def msg():
    mb=messagebox.showinfo("Alert","Click on OK")
    if mb=="ok":
        topwin()

b1=Button(root,text="Click to Start",command=msg)
b1.place(relx=0.3,rely=0.7)

def topwin():
    top=Toplevel()
    top.configure(bg="yellow")
    top.geometry("600x500")
    label=Label(root,text="Enter total amount:")
    entry=Entry(top)
    lbl=Label(top,text="Number of notes are:")
    l1=Label(top,text="2000")
    l2=Label(top,text="500")
    t1=Entry(top)
    t2=Entry(top)

    def calculator():
        global amount
        amount=int(entry.get())
        n2000=amount//2000
        amount%=2000
        n500=amount//500
        amount%=500
        t1.delete(0,END)
        t2.delete(0,END)
        t1.insert(END,str(n2000))
        t2.insert(END,str(n500))

    btn=Button(top,text="Calculate", command=calculator)
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    top.mainloop()

root.mainloop()