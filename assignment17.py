import tkinter as tk
def hello():
    print("HELLO WORLD")
demolabel ="GUI"
def demo_label(label):
    label.config(text=str(demolabel))
root = tk.Tk()
root.title("GUI 1")
root.geometry("200x100")
frame = tk.Frame(root)
frame.pack()
hello = tk.Button(frame,text="Hello",command=hello)
hello.pack(side=tk.LEFT)
button = tk.Button(frame,text="Exit",command=quit)
button.pack(side=tk.LEFT)
label = tk.Label(root)
label.pack()
demo_label(label)

from tkinter import*
root=Tk()
root.title("GUI 1")
root.geometry("200x100")
frame=Frame(root)
frame.pack()
Label(frame,text='Enter Name').grid(row=0)
Label(frame,text='Enter Age').grid(row=1)
e1=Entry(frame,bd=1)
e1.grid(row=0,column=1)
e2=Entry(frame,bd=1)
e2.grid(row=1,column=1)
def cal():
    a=e1.get()
    b=e2.get()
    c=a+ '' +b
    lb1=Label(frame,text=c)
    lb1.grid(row=2,column=1)
    lb1.config(text=a+b)
lb1=Label(frame,text='')
lb1.grid(row=2,column=1)
db=Button(frame,text='Enter',command=cal)
db.grid(row=4,column=1)
mainloop()

