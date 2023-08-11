import tkinter
from tkinter import messagebox
window=tkinter.Tk()
window.title("Question Set")
window.geometry('1000x500')
window.configure(bg="#AF125A")
def firstq():
    if(e1.get()=="James and Lily"):
        messagebox.showinfo(title="correct",message="Correct Answer")
    else:
        messagebox.showerror(title="Wrong",message="Your Answer is wrong")
def secondq():
    if(e2.get()=="Emma Watson"):
        messagebox.showinfo(title="correct",message="Correct Answer")
    else:
        messagebox.showerror(title="Wrong",message="Your Answer is wrong")
def thirdq():
    if(e3.get()=="snake"):
        messagebox.showinfo(title="correct",message="Correct Answer")
    else:
        messagebox.showerror(title="Wrong",message="Your Answer is wrong")
def fourthq():
    if(e4.get()=="griphook"):
        messagebox.showinfo(title="correct",message="Correct Answer")
    else:
        messagebox.showerror(title="Wrong",message="Your Answer is wrong")
def fifthq():
    if(e5.get()=="were wolf"):
        messagebox.showinfo(title="correct",message="Correct Answer")
    else:
        messagebox.showerror(title="Wrong",message="Your Answer is wrong")
def continueq():
    messagebox.askyesnocancel(title="continue",message="Do you want to continue?")


head=tkinter.Label(window,text="Harry Potter Questions",bg="#AF125A",fg="#C0F5FA",font=("Arial",30))
q1=tkinter.Label(window,text="When are the names of Harry Potter's parents?",bg="#AF125A",fg="#C0F5FA",font=("Arial",15))
e1=tkinter.Entry(window,font=("Arial",15))
b1=tkinter.Button(window,text="check",command=firstq,font=("Arial",15),fg="#582B11",bg="#87F1FF")
q2=tkinter.Label(window,text="Which artist played the character of Hermione Granger?",bg="#AF125A",fg="#C0F5FA",font=("Arial",15))
e2=tkinter.Entry(window,font=("Arial",15))
b2=tkinter.Button(window,text="check",command=secondq,font=("Arial",15),fg="#582B11",bg="#87F1FF")
q3=tkinter.Label(window,text="What animal can Harry speak to?",bg="#AF125A",fg="#C0F5FA",font=("Arial",15))
e3=tkinter.Entry(window,font=("Arial",15))
b3=tkinter.Button(window,text="check",command=thirdq,font=("Arial",15),fg="#582B11",bg="#87F1FF")
q4=tkinter.Label(window,text=" Who was the first goblin Harry ever met?",bg="#AF125A",fg="#C0F5FA",font=("Arial",15))
e4=tkinter.Entry(window,font=("Arial",15))
b4=tkinter.Button(window,text="check",command=fourthq,font=("Arial",15),fg="#582B11",bg="#87F1FF")
q5=tkinter.Label(window,text="What animal can Remus Lupin turn into?",bg="#AF125A",fg="#C0F5FA",font=("Arial",15))
e5=tkinter.Entry(window,font=("Arial",15))
b5=tkinter.Button(window,text="check",command=fifthq,font=("Arial",15),fg="#582B11",bg="#87F1FF")
b6=tkinter.Button(window,text="continue",command=continueq,font=("Arial",15),fg="#582B11",bg="#87F1FF")
head.grid(row=0,column=0,columnspan=3)
q1.grid(row=1,column=0)
e1.grid(row=1,column=1)
b1.grid(row=1,column=2)
q2.grid(row=2,column=0)
e2.grid(row=2,column=1)
b2.grid(row=2,column=2)
q3.grid(row=3,column=0)
e3.grid(row=3,column=1)
b3.grid(row=3,column=2)
q4.grid(row=4,column=0)
e4.grid(row=4,column=1)
b4.grid(row=4,column=2)
q5.grid(row=5,column=0)
e5.grid(row=5,column=1)
b5.grid(row=5,column=2)
b6.grid(row=6,column=0,columnspan=3)
for i in range(7):
    window.grid_rowconfigure(i,weight=1)
for i in range(3):
    window.grid_columnconfigure(i,weight=1)
window.mainloop()